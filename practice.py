from PIL import Image




with open ("elevation_small.txt") as file:
    raw_data = file.readlines()
    clean_data = [row.split() for row in raw_data]
    
    print(clean_data)





bk = Image.new('RGBA', (300, 300), 'black')
bk.getpixel((0,0))
for x in range(10):
    for y in range(10):
        bk.putpixel((x, y), (210, 210, 210))
bk.save('test_black.png')







