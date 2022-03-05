import os
import urllib.request



cwd = os.getcwd()


imgNum = input('Enter number of images: ')
imgDim = input('Enter image size (e.g. 1920x1080): ').split('x')


os.chdir(cwd)


for i in range(1, int(imgNum) + 1):
	i = str(i)
	urllib.request.urlretrieve(('https://picsum.photos/' + imgDim[0] + '/' + imgDim[1] + '?random'), ('stock-image-' + i + '.jpg'))
