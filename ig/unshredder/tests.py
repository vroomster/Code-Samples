# Just fix it so that it just does the tokyo image, that it figures out where the shreds are
# Improve shred finding algorithm

#answer = [8, 10, 14, 16, 18, 13, 7, 3, 2, 11, 4, 19, 17, 12, 6, 15, 1, 5, 0, 9]
orig_path = './images/originals/'
unshred_path = './images/unshred/'
file_types = ('*.png', '*.jpg') # image file types to grab


def check_images():
  for i in range(width):
    	for j in range(height):
    	  if orig_data[j*width + i] != unshred_data[j*width + i]:
    	    print "Images did not match!", i, j
    	    return False
  print "Match successful"
  return True



for i in range(1):
	execfile('shredder.py')
	execfile('unshredder.py')
	orig_files = []
	unshred_files = []
	for file_type in file_types:
		orig_files.extend(glob.glob(orig_path + file_type))

	for image_file in orig_files:
		orig_image = Image.open(image_file)
		print image_file
		unshred_image = Image.open(unshred_path + os.path.split(image_file)[1])
		print unshred_path + os.path.split(image_file)[1]
		width, height = orig_image.size 
		width1, height1 = unshred_image.size
		orig_data = orig_image.getdata()
		unshred_data = unshred_image.getdata()
		if height != height1 or width != width1:
			print "Images are not same size", image_file
		if not check_images():
		  break

    
    
      



#  unshred()
#  if unshredded != answer:
#    print "Failure!"
#  unshredded = []
#  shredded = range(width/shred_width)

#print "Done with 100 tries"
  #print unshredded
  #print shredded