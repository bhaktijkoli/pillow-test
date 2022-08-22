from turtle import end_fill
from PIL import Image
import datetime as dt
import os


def generate_thumbnail(file, filename):
    image = Image.open(file)
    h, w = image.height, image.width
    MAX = max(h, w)
    req = 200
    if MAX > 200:
        new_h, new_w = int((req/MAX)*h), int((req/MAX)*w)
        image = image.resize((new_w, new_h), Image.ANTIALIAS)
    if image.mode in ['P', 'RGBA']:
        image = image.convert('RGB')
    image.save("optimized.jpeg", 'JPEG', optimize=True)


total = 0
timings = {}

files = os.listdir('inputs')
for file in files:
    if file.endswith('.png') or file.endswith('.jpg'):
        start = dt.datetime.now()
        image = Image.open(f"inputs/{file}")
        h, w = image.height, image.width
        MAX = max(h, w)
        req = 200
        if MAX > 200:
            new_h, new_w = int((req/MAX)*h), int((req/MAX)*w)
            image = image.resize((new_w, new_h), Image.ANTIALIAS)
        if image.mode in ['P', 'RGBA']:
            image = image.convert('RGB')
        image.save(f"outputs/{file}.jpeg", 'JPEG', optimize=True)
        end = dt.datetime.now()
        diff = (end-start).total_seconds() * 1000
        timings[file] = diff
        print(f"Finished converting {file} in {diff}ms")
        total += diff

print(f"Completed converting all files in {total}ms")
# start = dt.datetime.now()
# generate_thumbnail()
# end = dt.datetime.now()
# diff = (end-start).total_seconds() * 1000
# print(f"Finished in {diff}ms")
