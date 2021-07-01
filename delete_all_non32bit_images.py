from PIL import Image
import os
currentpath = "D:\\hitomi\\to sort\\bg\\"
print (currentpath)

list = []

os.chdir(currentpath)
for root, dirs, files in os.walk(".", topdown = False):
	for name in files:
		a = os.path.join(root, name)
		list += [a]
print (list)
path = currentpath
for x in range(len(list)):
	line = path + list[x][2:]
	print (line)


	img = Image.open(str(line), 'r' )
	print( line )
	has_alpha = img.mode == 'RGBA'
	print( has_alpha, line )
	img.close()
	if has_alpha != True:
		os.remove(str(line))