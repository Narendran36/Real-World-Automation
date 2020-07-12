#!/usr/bin/env python3
import requests
import os
import re

files = [f for f in os.listdir("supplier-data/images") if re.match(r'.*\.jpeg', f)]

url = "http://localhost/upload/"

for f in files:
        with open('supplier-data/images/'+f, 'rb') as opened:
                r = requests.post(url, files={'file': opened})