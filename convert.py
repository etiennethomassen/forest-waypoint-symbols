import os
from PIL import Image
from pixels2svg import pixels2svg

# Open csv file
csv = open('lijst.csv','w')
# Read list of files from png directory and sort file names
lijst = os.listdir('png')
lijst.sort()
for i, file in enumerate(lijst):
    if file.lower().endswith(".png"):

        # read file
        filename = file.split('.')[0]
        img_src = os.path.join('png', file)
        img = Image.open(img_src)

        # Background color
        bg_img = Image.new('RGB', (32, 32), 'magenta')  # RGBA Magenta is 255, 0, 255, 255

        # Paste image upon background
        bg_img.paste(img, (0,0), img)

        # save image for Garmin
        outfile = 'Custom ' + str(i) + '.bmp'
        img_garmin = os.path.join('garmin', outfile)
        bg_img.save(img_garmin)

        # save image for BaseCamp
        outfile = '{:0>7}'.format(str(i) + '.bmp')
        img_garmin = os.path.join('basecamp', outfile)
        bg_img.save(img_garmin)

        # convert to svg and save
        outfile = filename + '.svg'
        img_svg = os.path.join('svg', outfile)
        svg_img = pixels2svg(img_src, img_svg)

        # write to csv for reference of number to name
        regel = str(i) + ';' + file + '\n'
        csv.write(regel)

csv.close()
