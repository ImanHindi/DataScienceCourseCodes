## create directories
#dataset_home = 'dataset_dogs_vs_cats/'
#subdirs = ['train/', 'test/']
#for subdir in subdirs:
#	# create label subdirectories
#	labeldirs = ['dogs/', 'cats/']
#	for labldir in labeldirs:
#		newdir = dataset_home + subdir + labldir
#		makedirs(newdir, exist_ok=True)
#
#seed(1)
## define ratio of pictures to use for validation
#val_ratio = 0.25
## copy training dataset images into subdirectories
#src_directory = 'train/'
#for file in os.listdir(src_directory):
#	src = src_directory + '/' + file
#	dst_dir = 'train/'
#	if random() < val_ratio:
#		dst_dir = 'test/'
#	if file.startswith('cat'):
#		dst = dataset_home + dst_dir + 'cats/'  + file
#		copyfile(src, dst)
#	elif file.startswith('dog'):
#		dst = dataset_home + dst_dir + 'dogs/'  + file
#		copyfile(src, dst)