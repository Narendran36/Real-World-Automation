#!/usr/bin/env python3

import os
from PIL import Image
import re

files = [f for f in os.listdir("supplier-data/images") if re.match(r'.*\.tiff', f)]

size = 600,400
for f in files:
        im = Image.open("supplier-data/images/"+f).convert('RGB')
        im.resize((size)).save("supplier-data/images/"+f.split(".")[0]+".jpeg","JPEG")
