from PIL import Image


class Map:

    def __init__(self, data):
        self.data = data
        self.min_elevation = min(self.data)
        self.max_elevation = max(self.data)
        self.brightness_list = []

        

    def get_elevation_data(self, data):    
        with open ("elevation_small.txt") as file:
            data = file.read().split()
            data = [int(i) for i in data]
            # clean_data = [row.split() for row in data]

    # def get_max_elevation(self):
    #     return max(self.data)

    # def get_min_elevation(self):
    #     return min(self.data)
    
    def create_brightness_list(self):
        # Converts list of elevation numbers to pixel objects (RGBA)

        self.brightness_list = []
        count = 0
        x = 0
        y = 0
        for elevation in data:
            color = self.get_brightness(elevation)
            self.brightness_list.append(color)
            count += 1
            if x == 600:
                x = 0
                y += 1
        




    def draw_map(self):
        # Converts self.brightness_list to picture
        image = Image.new('RGBA', (600, 600), (0, 0, 0, 255))
        image.getpixel((0, 0))
        count = 0
        self.create_brightness_list()
        for x in range(600):
            for y in range(600):
                print(self.brightness_list[count])
                image.putpixel((y, x), (self.brightness_list[count]))
                count += 1
        image.save('test_black.png')
        image.show()

    def get_brightness(self, elevation):
        brightness = (elevation - self.min_elevation) / (self.max_elevation - self.min_elevation)
        greyscale = int(255 * brightness)
        return (greyscale, greyscale, greyscale, 255)
   


with open ("elevation_small.txt") as file:
    data = file.read().split()
    data = [int(i) for i in data]

our_data = data

map1 = Map(our_data)

# print(data)

map1.draw_map()

# print(len(data))

# print(map1.get_brightness(4688))

# map1.create_brightness_list()








