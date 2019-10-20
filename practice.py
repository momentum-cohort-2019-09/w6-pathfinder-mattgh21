from PIL import Image
from PIL import ImageColor


class Map:

    def __init__(self, data):
        self.data = data
        self.min_elevation = min(self.data)
        self.max_elevation = max(self.data)
        self.brightness_list = []
        self.elevation_grid = []
        self.image = Image.new('RGBA', (600, 600), (0, 0, 0, 255))

    
    def get_elevation_data(self, data):    
        with open ("elevation_small.txt") as file:
            data = file.read().split()
            data = [int(i) for i in data]
            # clean_data = [row.split() for row in data]

    
    def create_brightness_list(self):
        # Converts list of elevation numbers to pixel objects (RGBA)
        count = 0
        for column in range (600):
            current_elevation_row = []
            current_brightness_row = []
            for row in range (600):
                current_elevation_row.append(self.data[count])
                current_brightness_row.append(self.get_brightness(self.data[count]))
                count += 1
            self.brightness_list.append(current_brightness_row)
            self.elevation_grid.append(current_elevation_row)
        # print(self.brightness_list)
        # print(self.elevation_grid)

        

        # for elevation in data:
        #     pixel_color = self.get_brightness(elevation)
        #     self.brightness_list.append(pixel_color)
           
        
    def find_path(self, y_coord):
        # right = 
        # up_right = 
        # down_right = 
        for x in range (600):
            self.image.putpixel((x, 300), ImageColor.getcolor('blue', 'RGBA'))
        

    def draw_map(self):
        # Converts self.brightness_list to picture
        self.image.getpixel((0, 0))
        self.create_brightness_list()
        for x in range(600):
            for y in range(600):
                self.image.putpixel((y, x), (self.brightness_list[x][y]))
                # self.find_path(300)


    def save_map(self):
        self.image.save('new_map.png')
        self.image.show()

    def get_brightness(self, elevation):
        brightness = (elevation - self.min_elevation) / (self.max_elevation - self.min_elevation)
        color = int(255 * brightness)
        return (color, color, color, 255)
   

class Path:
    def __init__(self, elevation, map):
        self.map = map1
        self.elevation = elevation

    




with open ("elevation_small.txt") as file:
    data = file.read().split()
    data = [int(i) for i in data]




our_data = data

map1 = Map(our_data)

# print(data)

map1.draw_map()

map1.find_path(300)

map1.save_map()







