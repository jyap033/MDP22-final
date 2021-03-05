from os import read
import pygame
from Exploration import Exploration_simulation
from Map import Preprocess_Map
from timer import timer
from read_txt import read_txt

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

WIDTH = 400
HEIGHT = 600

class Spot:
    def __init__(self,row,col,size,color):
        self.row=row
        self.col=col
        self.size=size
        self.color=color
    def draw(self,row,col,size,win,color):
        pygame.draw.rect(win, color, (col*size, row*size, size, size))
        pygame.draw.line(win, GREY, (col*size, row* size), ((col+1)*size, row* size))
        pygame.draw.line(win, GREY, (col*size, row * size), (col*size, (row+1)* size))
    def make_obstacle(self,color):
        self.color=BLACK
    def make_end(self,end):
        self.color=ORANGE


class Simulator_Exploration:
    def draw_grid(self, win, cols, rows,width,height):
        gap =width//cols
        for i in range(rows):
            pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
            for j in range(cols):
                pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, height))

    def draw_rectangle(self,current,color,size,win):
        row=current[0]
        col=current[1]
        pygame.draw.rect(win, color, (col*size, row*size, size, size))
        pygame.draw.line(win, GREY, (col*size, row* size), ((col+1)*size, row* size))
        pygame.draw.line(win, GREY, (col*size, row * size), (col*size, (row+1)* size))



    def make_grid(self, rows,cols,size,matrix):
        grid = []
        for i in range(rows):
            grid.append([])
            for j in range(cols):
                if matrix[i][j]==3:
                    spot = Spot(i, j,size,YELLOW)
                elif matrix[i][j]==1:
                    spot = Spot(i, j,size,BLACK)
                else:
                    spot = Spot(i, j,size,WHITE)
                grid[i].append(spot)
        return grid

    def draw_robot(self,current,size,direction):
        row=current[0]
        col=current[1]
        robot=[]
        for i in range(row-1,row+2):
            for j in range(col-1,col+2):
                if direction=='N' and i==row-1 and j==col:
                    spot=Spot(i,j,size,TURQUOISE)
                elif direction=='S' and i==row+1 and j==col:
                    spot=Spot(i,j,size,TURQUOISE)
                elif direction=='E' and i==row and j==col+1:
                    spot=Spot(i,j,size,TURQUOISE)
                elif direction=='W' and i==row and j==col-1:
                    spot=Spot(i,j,size,TURQUOISE)
                else:
                    spot=Spot(i,j,size,BLUE)
                robot.append(spot)
        return robot

    def update_map(self,row,col,size,matrix,pos,direction,WIN):
        grid=self.make_grid(row,col,size,matrix)
        for List in grid:
            for item in List:
                item.draw(item.row,item.col,item.size,WIN,item.color)
        robot=self.draw_robot(pos, size,direction)        
        for ele in robot:
            ele.draw(ele.row,ele.col,ele.size,WIN,ele.color)