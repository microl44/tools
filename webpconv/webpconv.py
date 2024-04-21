from PIL import Image
import os
import sys
import subprocess

source = sys.argv[1]
target = sys.argv[2]

files = os.listdir(source)

for file in files:
    if '.webp' in file:
        im = Image.open(os.path.join(source, file)).convert("RGB")
        if file != '.' and file != '..':
            im.save(os.path.join(target, (file.split('.')[0] + ".png")), 'png')