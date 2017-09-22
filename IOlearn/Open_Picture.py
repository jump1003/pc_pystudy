# import PIL.Image as pic
# pic1 = pic.open(r'C:\Users\Jump hu\Pictures\lovewallpaper\188364-106.jpg')
# pic1.show()

# with open(r'C:\Users\Jump hu\Desktop\test.txt', 'r') as f:
# 	a=f.read()
# 	with open(r'C:\Users\Jump hu\Desktop\test.txt', 'w'):
# 		with open (r'C:\Users\Jump hu\Desktop\test.txt', 'a') as fi:
# 			fi.write(a.replace('a', 'e'))
from io import StringIO
f = StringIO('hi\nJump!\nbye-bye,Jump!')
while True:
	l = f.readline()
	if l =='':
		break
	print(l.strip())