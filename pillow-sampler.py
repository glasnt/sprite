#!/usr/bin/env python

import sys
from PIL import Image

im = Image.open(sys.argv[1])
im = im.convert('RGB')
im = im.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.ROTATE_270)

print("<div class='palette'><code>")
histo = im.getcolors()

# if sampling fails, drop count https://stackoverflow.com/questions/1065945/how-to-reduce-color-palette-with-pil
# using 32 here as POC
if not histo:
    im = im.convert('P', palette=Image.ADAPTIVE, colors=32)
    im = im.convert('RGB')

histo = im.getcolors()
print(histo)
print(len(histo))
print("</code></div><br><hr><br>")

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

stars = "▷◼︎✤✷✽❤︎✰❐❄︎➤⬆︎⬇︎♠︎♣︎♥︎♦︎♞♟✝︎☘︎"
# TODO - monospace friendly stars
#stars = "abcdefghijklmnopqrstuvwxyz"
#stars = "abc
#stars = "███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████"

if len(sys.argv) == 3:
    step = int(sys.argv[2])
else:
    step = 1

for idx, x in enumerate(histo):
    h = rgb2hex(x[1])
    chart[h] = stars[idx % len(stars)]

style = """
<style>
table {
    border-collapse: collapse;
}

table, th, td {
    border: 1px solid black;
}

td { 
    vertical-align: middle;
    text-align: center;
    height: 30px;
    width: 30px
}
</style>
"""
print(style)
print("<table  class='chart'>")
for x in range(0, im.width, step):
    print("<tr>")
    for y in range(0, im.height, step):
        p = rgb2hex(im.getpixel((x,y))) 
        print("<td style='color: {}'>{}</td>".format(p, chart[p]), end="")
    print("</tr>")
    #print("")
print("</table>")
