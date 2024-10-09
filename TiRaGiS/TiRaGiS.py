#abandon hope all ye who enter here

import math
import random

def print_matrix(matrix) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print()
             

HEIGHT = 10
WIDTH = 10

class CITY:
    def __init__(self, coord) -> None:
        self.coord = coord #x, y

class WORLD:
    def __init__(self) -> None:
        self.MAP_CITIES = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.LIST_CITIES = []
        
        for _ in range(round(math.log2(WIDTH * HEIGHT))):
            while True:
                x, y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
                if self.MAP_CITIES[y][x] == " ":
                    self.LIST_CITIES.append(CITY([x, y]))
                    self.MAP_CITIES[y][x] = len(self.LIST_CITIES) - 1
                    break
                

a = WORLD()
print_matrix(a.MAP_CITIES)