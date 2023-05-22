import os
from cairosvg import svg2png

for filename in os.listdir('input'):
    f = open(f'input/{filename}', 'rb')

    content = f.read()
    name = f.name.split('/')[1].split('.')[0]

    svg2png(bytestring=content, write_to=f'output/{name}.png')