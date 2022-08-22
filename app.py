from PIL import Image
import datetime as dt


def generate_thumbnail():
    image = Image.open("original.png")
    h, w = image.height, image.width
    MAX = max(h, w)
    req = 200
    if MAX > 200:
        new_h, new_w = int((req/MAX)*h), int((req/MAX)*w)
        image = image.resize((new_w, new_h), Image.ANTIALIAS)
    if image.mode in ['P', 'RGBA']:
        image = image.convert('RGB')
    image.save("optimized.jpeg", 'JPEG', optimize=True)


start = dt.datetime.now()
generate_thumbnail()
end = dt.datetime.now()
diff = (end-start).total_seconds() * 1000
print(f"Finished in {diff}ms")
