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
        self.best_elev_delta = 10000000000000
        self.best_y = 0

    
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
           
    def get_next_y(self, x, y_coord):
        current_position = self.elevation_grid[x][y_coord]
        if x >= 599:
            return -1
        else: 
            right = abs((self.elevation_grid[y_coord][x+1]) - current_position)

        if y_coord == 0:
            up_right = 10000000000000
        else:
            up_right = abs((self.elevation_grid[y_coord-1][x+1]) - current_position)

        if y_coord == 599:
            down_right = 1000000000000 
        else:   
            down_right = abs((self.elevation_grid[y_coord+1][x+1]) - current_position)

        min_val = min(right, up_right, down_right)

        
        if min_val == right:
            return y_coord
        elif min_val == down_right:
            return y_coord + 1
        elif min_val == up_right:
            return y_coord - 1

        
    def find_path(self, y_coord):
        cur_elev_delta = 0
        cur_y = y_coord
        for x in range (600):   
            self.image.putpixel((x, y_coord), ImageColor.getcolor('blue', 'RGBA'))
            y = y_coord
            y_coord = self.get_next_y(x, y_coord)
            # Do something with cur_elev..
            if x < 599:
                cur_elev_delta += abs(self.elevation_grid[x][y] - self.elevation_grid[x+1][y_coord])

        # compare self.best_elev_delta and cur_elev_delta
        if cur_elev_delta < self.best_elev_delta:
            self.best_elev_delta = cur_elev_delta
            self.best_y = cur_y
        print(self.best_y)
        print(self.best_elev_delta)

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
   

with open ("elevation_small.txt") as file:
    data = file.read().split()
    data = [int(i) for i in data]

our_data = data

map1 = Map(our_data)

# print(data)

map1.draw_map()

for y_coord in range(600):
    map1.find_path(y_coord)

y_coord = map1.best_y
for x in range (600):   
    map1.image.putpixel((x, y_coord), ImageColor.getcolor('red', 'RGBA'))
    y_coord = map1.get_next_y(x, y_coord)

map1.save_map()







