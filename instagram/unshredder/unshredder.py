# coding: utf-8
# Author: Varun Bandi
# Date: 1/18/2012
# Usage: python unshredder.py <input image name>
# Purpose: Unshredding programming puzzle -- See problem Text
# Solution: Calculate where the shreds are, assumes uniform widths
#     then starting with one shred, figure out best fit shred to go to left or right of it
#     repeat until all shreds are attached
from PIL import Image
import sys

# User set heuristics to be used in algorithm
slice_width = 3
shred_threshold = 1.25

# This could be optomized by going to an array of the first n primes
prime_factors = []

# Checks if i is prime_factor by checking if any previoussaved
#   prime factor divides it
def is_prime_factor(i): return not any(i%factor == 0 for factor in prime_factors)	

# Calculates the position of all possible shreds
# TODO possibly a better way to do this??
def possible_shred_positions():
  shred_positions = set([])
  for i in range(2, width/2):	
		if width % i == 0 and is_prime_factor(i):
			prime_factors.append(i)      			
			for j in range(i, width, i):
				shred_positions.add(j-1)	
  return shred_positions


# calculate borders of the shreds (this allows for variable shred lengths)
def calc_shreds():			
	shred_positions = possible_shred_positions()
	shred_left_border = 0	
	for j in sorted(shred_positions):
		left_slice_diff = avg_edge_diff(j, 2, False)
		right_slice_diff = avg_edge_diff(j+1, 2, True)
		avg_diff = (left_slice_diff + right_slice_diff)/2
		if edge_diff(j,j+1) > (avg_diff * shred_threshold):
			shreds.update({shred_left_border:j})
			shred_left_border = j+1
	shreds.update({shred_left_border:width-1})


def unshred_left_border(): return unshredded[0][0]
def unshred_right_border(): return unshredded[len(unshredded)-1][1]
def get_pixel_value(x, y): return data[y * width + x]
		
#Calculate absolute difference between pixel values
def pixel_diff(p1, p2): return reduce(lambda x,y: x+y, map (lambda x,y: abs(x-y), p1, p2))

#Calculate the pixel difference between 2 columns in the image
def edge_diff(x1, x2):
	diff = edge_diffs.setdefault((x1,x2))
	if diff == None:
		diff = 0
		for i in range(0, height):		 
		  diff += pixel_diff(get_pixel_value(x1, i), get_pixel_value(x2, i))		 				
		edge_diffs[(x1,x2)] = diff
	return diff

# An avg edge diff is a running average of the diff 
# between consecutive columns going in either left or right direction
def avg_edge_diff(x, num_columns, right):
	diff_sum = 0
	for i in range(0, num_columns-1):
		diff_sum += edge_diff(x + (i if right else -i), x + (i+1 if right else -(i+1)))
	return diff_sum/(num_columns-1)


# Find best shreds that fit the left and right borders of unshredded picture
def find_best_fit((left_fit_diff,left_fit_piece), (right_fit_diff, right_fit_piece)):			
	if left_fit_piece == None:
		left_slice_diff = avg_edge_diff(unshred_left_border(), slice_width, True)
		for left, right in shreds.iteritems():
			left_edge_diff = edge_diff(unshred_left_border(), right)		
			if abs(left_edge_diff - left_slice_diff) < left_fit_diff:
				left_fit_diff, left_fit_piece = abs(left_edge_diff - left_slice_diff), (left, right) 
	
	if right_fit_piece == None:
		right_slice_diff = avg_edge_diff(unshred_right_border(), slice_width, False)
		for left, right in shreds.iteritems():
			right_edge_diff = edge_diff(unshred_right_border(), left)		
			if abs(right_edge_diff - right_slice_diff) < right_fit_diff:
				right_fit_diff, right_fit_piece =  abs(right_edge_diff - right_slice_diff), (left, right)
	return (left_fit_diff, left_fit_piece), (right_fit_diff, right_fit_piece)

# Main method that unshreds the picture by finding next best possible fitting shred
def unshred():
	calc_shreds()
	unshredded.append(shreds.popitem())	
	(left_fit_diff,left_fit_piece), (right_fit_diff, right_fit_piece) = (sys.maxint, None), (sys.maxint, None)
	while len(shreds) > 0:
		((left_fit_diff,left_fit_piece), (right_fit_diff, right_fit_piece)) = find_best_fit((left_fit_diff,left_fit_piece), (right_fit_diff, right_fit_piece))
		if left_fit_diff < right_fit_diff:
		  unshredded.insert(0, left_fit_piece)
		  del shreds[left_fit_piece[0]] 
		  left_fit_diff, left_fit_piece = (sys.maxint, None)
		else:
			unshredded.append(right_fit_piece)
			del shreds[right_fit_piece[0]]
			right_fit_diff, right_fit_piece = (sys.maxint, None)


#The actual gritty details to unshred the given picture
unshredded = []
shreds = {}
edge_diffs = {}

image = Image.open(sys.argv[1])
data = image.getdata() # This gets pixel data  
width, height = image.size  
  
unshred()

unshredded_image = Image.new('RGBA', image.size)
j,k = 0,0
for left,right in unshredded:
  source_region = image.crop( (left, 0, right+1, height) )
  destination_point = (j, k)	
  unshredded_image.paste(source_region, destination_point)
  j += (right-left+1)

# Output the new image
#unshredded_image.save('unshredded.jpg', 'JPEG')
unshredded_image.save('unshredded.png')



