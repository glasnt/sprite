#!/usr/bin/env python

import sys
from PIL import Image


im = Image.open(sys.argv[1])
im = im.convert('RGB')

histo = im.getcolors()
print(histo)
print(len(histo))


def rgb2hex(pix):
    if len(pix) == 4:
        r, g, b = pix[1:]
    else:
        r, g, b = pix
    _hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return _hex

#import pdb; pdb.set_trace()
histo = im.getcolors()
chart = {}
#TODO - histo to 'chart'

#stars = "▷◼︎✤✷✽❤︎✰❐❄︎➤⬆︎⬇︎♠︎♣︎♥︎♦︎♞♟✝︎☘︎"
stars = "abcdefghijklmnopqrstuvwxyz"


if len(sys.argv) == 3:
    step = int(sys.argv[2])
else:
    step = 1

for idx, x in enumerate(histo):
    h = rgb2hex(x[1])
    chart[h] = stars[idx]


count = 0
for x in range(0, im.width, step):
    for y in range(0, im.height, step):
        count += 1
        p = rgb2hex(im.getpixel((x,y))) 
        print(chart[p], end="")
    print("")

print("Pixel count: {}".format(count))
