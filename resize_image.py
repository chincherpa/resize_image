from PIL import Image
import sys
import os

##new_width, file = sys.argv[1:]

new_width, file = 2000, r"D:\OneDrive\python_scripts\resize_image\chutesladders.png"

im = Image.open(file)
w, h = im.size


base = os.path.basename(file)
outfile = os.path.splitext(base)[0]

# print(outfile)
print(w, h)
w2 = w // 2
h2 = h // 2
print(w2, h2)

##imgScale = int(new_width)/w
##newWidth = int(w*imgScale)
##newHeight = int(h*imgScale)
##size = (newWidth, newHeight)

# im.resize(size, resample=0)
##img = im.resize(size, Image.ANTIALIAS)
##img.save(outfile + '.png', "PNG")

img = im.crop((0, 0, w2, h2))
img.save(outfile + '_crop.png', "PNG")
