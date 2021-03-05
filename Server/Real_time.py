from os import read
import pygame
from Exploration import Exploration_simulation
from Map import Preprocess_Map
from timer import timer
from read_txt import read_txt
from actual_exploration import exploration

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

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

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

    def get_pos(self,pos,size):
        y, x = pos
        row = x // size
        col = y // size
        return row, col
    def update_map(self,row,col,size,matrix,pos,direction):
        grid=self.make_grid(row,col,size,matrix)
        for List in grid:
            for item in List:
                item.draw(item.row,item.col,item.size,WIN,item.color)
        robot=self.draw_robot(pos, size,direction)        
        for ele in robot:
            ele.draw(ele.row,ele.col,ele.size,WIN,ele.color)
    def return_to_start(self,rows,col,size,current,mat2,endtime,interval):
        map=Preprocess_Map()
        explore=Exploration_simulation()
        times=timer()
        path=explore.bfs(current,[18,1],mat2)
        path.pop(0)
        for item in path:
            current=[item[0],item[1]]
            self.update_map(rows,col,size,mat2,current,item[2])
            pygame.display.update()
            pygame.time.wait(interval)
            if times.checktime(endtime):
                return map.map_to_hex_p1(mat2),map.map_to_hex_p2(mat2)
        exp_percent=explore.check_explored_percentage(mat2)
        print("explored "+ str(exp_percent) +" percent")
        return map.map_to_hex_p1(mat2),map.map_to_hex_p2(mat2)



def main(WIN,WIDTH):
    mat2=[]
    ROWS = 20
    COLS = 15
    GAP=WIDTH/COLS
    
    time=times.compute_target(minutes,seconds)
    map=Preprocess_Map()
    explore=Exploration_simulation()
    simulate=Simulator_Exploration()
    exp=exploration()
    mat2=[[3 for i in range(15)] for j in range(20)]
    for i in range(17,20):
        for j in range(0,3):
            mat2[i][j]=0
    for i in mat2:
        print(i)
    start=[18,1]
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    
    
        not_equal=True
        direction='N'
        coors=[18,1,'N',False]
        count=0
        res=[]
        simulate.update_map(ROWS,COLS,GAP,mat2,start,coors[2])
        pygame.display.update()
        pygame.time.wait(300)

        exp.main_left_wall_hugging(coors,mat2,GAP,COLS,ROWS)
        

        start=exp.bfs_exploration(coors,mat1,mat2,ROWS,COLS,GAP,WIN)
        exp.return_to_start(start,mat1,mat2,ROWS,COLS,GAP,WIN)


        for i in mat2:
            print(i)

    pygame.quit()




    


a,b=main(WIN, WIDTH)
print(a)
print(b)



    