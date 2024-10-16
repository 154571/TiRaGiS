#abandon hope all ye who enter here

import math
import random

def print_matrix(matrix) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print()
             

HEIGHT = 30
WIDTH = 30

class CITY:
    def __init__(self, coord) -> None:
        self.coord = coord #x, y
        

class WORLD:
    def __init__(self) -> None:
        self.MAP_CITIES = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.MAP_RIVERS = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.MAP_PRE_CITIES = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

        self.LIST_CITIES = []
                
        begin_x = random.randint(0, WIDTH)
        begin_y = random.randint(0, HEIGHT)
        for i in range(max(round(math.log2(HEIGHT*WIDTH)), 1)):
            directions = []
            river_lenght = random.randint(round((HEIGHT+WIDTH)*0.1), round((HEIGHT+WIDTH)*0.4))
            if (((begin_y - river_lenght) < 0) or (self.MAP_RIVERS[max(0, begin_y - 1)][begin_x] == 1)) == False:
                directions.append(0)
            if (((begin_x - river_lenght) < 0) or (self.MAP_RIVERS[begin_y][max(0, begin_x-1)] == 1)) == False:
                directions.append(1)
            if ((begin_y + river_lenght > HEIGHT) or (self.MAP_RIVERS[min(HEIGHT, begin_y + 1)][begin_x] == 1)) == False:
                directions.append(2)
            if ((begin_x + river_lenght > WIDTH) or (self.MAP_RIVERS[begin_y][min(WIDTH, begin_x + 1)] == 1)) == False:
                directions.append(3)
            
            if not directions:
                begin_x = random.randint(0, WIDTH)
                begin_y = random.randint(0, HEIGHT)
                continue
            direction = random.choice(directions)
            if direction == 0:
                for j in range(river_lenght):
                    self.MAP_RIVERS[begin_y - j][begin_x] = 1
                begin_y = random.randint(begin_y - river_lenght, begin_y)
            if direction == 1:
                for j in range(river_lenght):
                    self.MAP_RIVERS[begin_y][begin_x - j] = 1
                begin_x = random.randint(begin_x - river_lenght, begin_x)
            if direction == 2:
                for j in range(river_lenght):
                    self.MAP_RIVERS[begin_y + j][begin_x] = 1
                begin_y = random.randint(begin_y, begin_y + river_lenght)
            if direction == 3:
                for j in range(river_lenght):
                    self.MAP_RIVERS[begin_y][begin_x - j] = 1
                begin_x = random.randint(begin_x, river_lenght + begin_x)

        
        
a = WORLD()
print_matrix(a.MAP_RIVERS)
