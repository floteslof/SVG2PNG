import os
from cairosvg import svg2png

WIDTH=128
HEIGHT=128

for filename in os.listdir('input'):
    f = open(f'input/{filename}', 'rb')

    content = f.read()
    name = f.name.split('/')[1].split('.')[0]

    svg2png(bytestring=content, write_to=f'output/{name}.png', parent_width=WIDTH, parent_height=HEIGHT)