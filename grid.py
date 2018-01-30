from PIL import Image
import os

# path
path = 'png'
listing = os.listdir(path)

# getting all path+filename in a list
npath=[]
im=[]

for infile in listing:
    if infile.lower().endswith(".png"):
        im.append(infile)
        npath.append(os.path.join(path, infile))
npath.sort()

# canvas image to paste images onto
canvas = Image.new('RGB', (500,500), 'white')
# blank image in case list is empty
blank = Image.new('RGB', (32,32), 'white')

# paste images on canvas
for i in range(0,500,50):
    for j in range(0,500, 50):
        try:
            im = Image.open(npath.pop(0))
            canvas.paste(im, (i, j), im)
        except IndexError:
            im = blank
            canvas.paste(im, (i, j))

    canvas.save('grid/grid.png')