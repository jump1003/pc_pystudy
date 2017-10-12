import os
def Find_char(filechar, Path = os.path.abspath('.')):
	#os.chdir(Path)
	# new_path = []
	#print('get in %s' %Path)
	for f in os.listdir(Path):
		os.chdir(Path)
		if os.path.isdir(f):
			Find_char(filechar,os.path.join(Path, f))
		# elif f.find(filechar) != -1:
		elif filechar in f:
			print(os.path.join(Path, f))


if __name__== '__main__':
	Find_char('.')
