from PIL import Image


# ``` with open(“elevation_small.txt”) as file_handler:
#       elevation_data = file_handler.readlines()
#   return elevation_data
# def topo_data(elevation_data):
#   # [[0, 0, 10], [1, 0,15]]
#   topo_data = []
#   for y, line in enumerate(elevation_data):
#       for x, data in enumerate(line.split(” “)):
#           topo_data.append([x, y, int(data.strip(“\n”))])
#   return topo_data
# data = elevation_data()
# coords = topo_data(data)
# print(coords[0])

class Map:

    def __init__(self, elevation_data):
        self.elevation_data = elevation_data
        self.min_elevation = min(self.elevation_data)
        self.max_elevation = max(self.elevation_data)
        self.brightness_list = []

    
    def get_elevation_data(self, elevation_data):    
        with open ("elevation_small.txt") as file:
            elevation_data = file.readlines()
            return elevation_data
            print(elevation_data)

    def list_of_lists(elevation_data):
        topo_data = []
        for y, line in enumerate(elevation_data):
            for x, data in enumerate(line.split(' ')):
                topo_data.append([x, y, int(data.strip("\n"))])
        return topo_data

            # data = file.read().split()
            # data = [int(i) for i in data]
            # clean_data = [row.split() for row in data]

    
    def create_brightness_list(self):
        # Converts list of elevation numbers to pixel objects (RGBA)
        self.brightness_list = []
        # count = 0
        # x = 0
        # y = 0
        for elevation in elevation_data:
            color = self.get_brightness(elevation)
            self.brightness_list.append(color)
            # count += 1
            # if x == 600:
            #     x = 0
            #     y += 1
            # print(x, y)
        

    def draw_map(self):
        # Converts self.brightness_list to picture
        image = Image.new('RGBA', (600, 600), (0, 0, 0, 255))
        image.getpixel((0, 0))
        count = 0
        self.create_brightness_list()
        for x in range(600):
            for y in range(600):
                # print(self.brightness_list[count])
                image.putpixel((y, x), (self.brightness_list[count]))
                count += 1
        image.save('test_black.png')
        image.show()

    def get_brightness(self, elevation):
        brightness = (elevation - self.min_elevation) / (self.max_elevation - self.min_elevation)
        color = int(255 * brightness)
        return (color, color, color, 255)
   

# with open ("elevation_small.txt") as file:
#     data = file.read().split()
#     data = [int(i) for i in data]

with open ("elevation_small.txt") as file:
    elevation_data = file.readlines()
    # return elevation_data

our_data = elevation_data

map1 = Map(our_data)

# print(data)

map1.draw_map()

# print(len(data))

# print(map1.get_brightness(4688))

# map1.create_brightness_list()


