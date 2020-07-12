#! /usr/bin/env python3

import os,requests,re,json

files = [f for f in os.listdir("supplier-data/descriptions") if re.match(r'.*\.txt', f)]
#print(files)
alll = []
d = {}
for file in files:
        d.clear()
        with open("supplier-data/descriptions/"+file) as f:
                lines = f.readlines()
                d["description"] = "".join(lines[2:]).strip()
                d["weight"] = int(lines[1].strip().strip('lbs'))
                d["name"] = lines[0].strip()
                d["image_name"] = file.strip('.txt')+'.jpeg'
                #alll.append(d)
                response = requests.post('http://localhost/fruits/',json=d)
                print(response.status_code)
