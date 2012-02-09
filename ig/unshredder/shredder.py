# coding: utf-8
from PIL import Image
import glob
import random
import os

orig_path = './images/originals/'
shreds_path = './images/shreds/'
file_types = ('*.png', '*.jpg') # image file types to grab
image_files = []

for file_type in file_types:
	image_files.extend(glob.glob(orig_path + file_type))

for image_file in image_files:
  image = Image.open(image_file)
  shredded = Image.new('RGBA', image.size)
  width, height = image.size
  left, right = 0,0
  shreds = []
  #generate random shreds 
  while True:
  	right += random.randint(20, max(width/20, 20))
  	if right < width:
  	  shreds.append((left, right))
  	else:
  		l,r = shreds[len(shreds)-1]
  		shreds[len(shreds)-1] = (l,width-1)  		
  		break
  	left = right+1
  	  
  #create new shuffled, shredded image
  random.shuffle(shreds)
  j,k = 0,0
  for left, right in shreds:
    source_region = image.crop( (left, 0, right+1, height) )
    destination_point = (j, k)
    shredded.paste(source_region, destination_point)
    j+=(right-left+1)	
  shredded.save(shreds_path + os.path.split(image_file)[1])	


# = range(0, SHREDS)
#random.shuffle(sequence)
