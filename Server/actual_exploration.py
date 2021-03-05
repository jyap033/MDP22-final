
from real_time_simulation import Spot
from real_time_simulation import Simulator_Exploration
import pygame
from Exploration import Exploration_simulation

class exploration:
    def update_map(self,current,message,mat2):
        front_left=int(message[0])
        front_mid=int(message[1])
        front_right=int(message[2])
        left_top=int(message[3])
        left_mid=int(message[4])
        right_top=int(message[5])
        row=current[0]
        col=current[1]
        direction=current[2]
        if direction=='N':
            if row-2<0:
                pass
            # update front #
            else:
                for i in range(row-2,row-5,-1):
                    for j in range(col-1,col+2):
                        if j==col-1 and (abs(i-row)-2)<front_left and i>=0 :
                            mat2[i][j]=0
                        elif j==col-1 and (abs(i-row)-2)==front_left and front_left<3 and i>=0:
                            mat2[i][j]=1
                        if j==col and (abs(i-row)-2)<front_mid and i>=0:
                            mat2[i][j]=0
                        elif j==col and (abs(i-row)-2)==front_mid and front_mid<3 and i>=0:
                            mat2[i][j]=1
                        if j==col+1 and (abs(i-row)-2)<front_right and i>=0:
                            mat2[i][j]=0
                        elif j==col+1 and (abs(i-row)-2)==front_right and front_right<3 and i>=0:
                            mat2[i][j]=1
            #update left#
            if col-2<0:
                pass    
            else:
                for i in range(row-1,row+1):
                    for j in range(col-2,col-5,-1):
                        if i==row-1 and abs(j-col)-2<left_top and j>=0:
                            mat2[i][j]=0
                        elif i==row-1 and abs(j-col)-2==left_top and left_top<3 and j>=0:
                            mat2[i][j]=1
                        if i==row and abs(j-col)-2<left_mid and j>=0:
                            mat2[i][j]=0
                        elif i==row and abs(j-col)-2==left_mid and left_mid<3 and j>=0:
                            mat2[i][j]=1
            # update right #
            if col+2>14:
                pass
            else:
                for i in range(row-1,row):
                    for j in range(col+2,col+5):
                        print(abs(i-col)-2)
                        if abs(j-col)-2<right_top and j<15:
                            mat2[i][j]=0
                        elif abs(j-col)-2==right_top and right_top<3 and j<15:
                            mat2[i][j]=1

        elif direction=='S':
            # update front
            if row+2>19:
                pass
            else:
                for i in range(row+2,row+5):
                    for j in range(col-1,col+2):
                        if j==col+1 and (abs(i-row)-2)<front_left and i<20 :
                            mat2[i][j]=0
                        elif j==col+1 and (abs(i-row)-2)==front_left and front_left<3 and i<20:
                            mat2[i][j]=1
                        if j==col and (abs(i-row)-2)<front_mid and i<20:
                            mat2[i][j]=0
                        elif j==col and (abs(i-row)-2)==front_mid and front_mid<3 and i<20:
                            mat2[i][j]=1
                        if j==col-1 and (abs(i-row)-2)<front_right and i<20:
                            mat2[i][j]=0
                        elif j==col-1 and (abs(i-row)-2)==front_right and front_right<3 and i<20:
                            mat2[i][j]=1
            # update left
            if col+2>14:
                pass    
            else:
                for i in range(row+1,row-1,-1):
                    for j in range(col+2,col+5):
                        if i==row+1 and abs(j-col)-2<left_top and j<15:
                            mat2[i][j]=0
                        elif i==row+1 and abs(j-col)-2==left_top and left_top<3 and j<15:
                            mat2[i][j]=1
                        if i==row and abs(j-col)-2<left_mid and j<15:
                            mat2[i][j]=0
                        elif i==row and abs(j-col)-2==left_mid and left_mid<3 and j<15:
                            mat2[i][j]=1
            # update right
            if col-2<0:
                pass
            else:
                for i in range(row+1,row,-1):
                    for j in range(col-2,col-5,-1):
                        if abs(j-col)-2<right_top and j>=0:
                            mat2[i][j]=0
                        elif abs(j-col)-2==right_top and right_top<3 and j>=0:
                            mat2[i][j]=1

        
        elif direction=='E':
            # check front
            if col+2>19:
                pass
            else:
                for i in range(row-1,row+2):
                    for j in range(col+2,col+5):
                        if i==row-1 and abs(j-col)-2<front_left and j<15:
                            mat2[i][j]=0
                        elif i==row-1 and abs(j-col)-2==front_left and front_left<3 and j<15:
                            mat2[i][j]=1
                        if i==row and abs(j-col)-2<front_mid and j<15:
                            mat2[i][j]=0
                        elif i==row and abs(j-col)-2==front_mid and front_mid<3 and j<15:
                            mat2[i][j]=1
                        if i==row+1 and abs(j-col)-2<front_right and j<15:
                            mat2[i][j]=0
                        elif i==row+1 and abs(j-col)-2==front_right and front_right<3 and j<15:
                            mat2[i][j]=1
            # check left
            if row-2<0:
                pass
            else:
                for i in range(row-2,row-5,-1):
                    for j in range(col+1,col-1,-1):
                        if j==col+1 and abs(i-row)-2<left_top and i>=0:
                            mat2[i][j]=0
                        elif j==col+1 and abs(i-row)-2==left_top and left_top<3 and i>=0:
                            mat2[i][j]=1
                        if j==col and abs(i-row)-2<left_mid and i>=0:
                            mat2[i][j]=0
                        elif j==col and abs(i-row)-2==left_mid and left_mid<3 and i>=0:
                            mat2[i][j]=1
            # check right
            if row+2>19:
                pass
            else:
                for i in range(row+2, row+5):
                    for j in range(col+1,col+2):
                        if abs(i-row)-2<right_top and i<20:
                            mat2[i][j]=0
                        elif abs(i-row)-2==right_top and right_top<3 and i<20:
                            mat2[i][j]=1

        # facing west
        else:
            if col-2<0:
                pass
            else:
                for i in range(row-1,row+2):
                    for j in  range(col-2,col-5,-1):
                        if i==row+1 and abs(j-col)-2<front_left and j>=0:
                            mat2[i][j]=0
                        elif i==row+1 and abs(j-col)-2==front_left and front_left<3 and j>=0:
                            mat2[i][j]=1
                        if i==row and abs(j-col)-2<front_mid and j>=0:
                            mat2[i][j]=0
                        elif i==row and abs(j-col)-2==front_mid and front_mid<3 and j>=0:
                            mat2[i][j]=1
                        if i==row-1 and abs(j-col)-2<front_right and j>=0:
                            mat2[i][j]=0
                        elif i==row-1 and abs(j-col)-2==front_right and front_right<3 and j>=0:
                            mat2[i][j]=1
            if row+2>19:
                pass
            else:
                for i in range(row+2,row+5):
                    for j in range(col-1,col+1):
                        if j==col-1 and abs(i-row)-2<left_top and i<20:
                            mat2[i][j]=0
                        elif j==col-1 and abs(i-row)-2==left_top and left_top<3 and i<20:
                            mat2[i][j]=1
                        if j==col and abs(i-row)-2<left_mid and i<20:
                            mat2[i][j]=0
                        elif j==col and abs(i-row)-2==left_mid and left_mid<3 and i<20:
                            mat2[i][j]=1
            if row-2<0:
                pass
            else:
                for i in range(row-2, row-5,-1):
                    for j in range(col-1,col):
                        if abs(i-row)-2<right_top and i>=0:
                            mat2[i][j]=0
                        elif abs(i-row)-2==right_top and right_top<3 and i>=0:
                            mat2[i][j]=1


    def check_fully_explored(self,mat2):
        explored=True
        for i in range(len(mat2)):
            for j in range(len(mat2[0])):
                if mat2[i][j]==3:
                    explored=False
                    return explored
        return explored
        
    # check whether there is a wall to the left in case of obstacle, after updating the matrix.
    # returns True if obstacle is present, returns false if no obstacle is there
    def mat_check_left(self,current,mat2):
        row=current[0]
        col=current[1]
        direction=current[2]
        if direction=='N':
            new_col=col-2
            if new_col<0:
                return True
            side=[[row-1,new_col],[row,new_col],[row+1,new_col]]
            for item in side:
                if mat2[item[0]][item[1]]==1:
                    return True
            return False
        elif direction=="S":
            new_col=col+2
            if new_col>14:
                return True
            side=[[row-1,new_col],[row,new_col],[row+1,new_col]]
            for item in side:
                if mat2[item[0]][item[1]]==1:
                    return True
            return False
        elif direction=='E':
            new_row=row-2
            if new_row<0:
                return True
            side=[[new_row,col-1],[new_row,col],[new_row,col+1]]
            for item in side:
                if mat2[item[0]][item[1]]==1:
                    return True
            return False
        else:
            new_row=row+2
            if new_row>19:
                return True
            side=[[new_row,col-1],[new_row,col],[new_row,col+1]]
            for item in side:
                if mat2[item[0]][item[1]]==1:
                    return True
            return False
    # check whether there is a wall to the front in case of obstacle, after updating the matrix.
    # returns True if obstacle is present, returns false if no obstacle is there
    
    def mat_check_front(self,current,mat2):
        row=current[0]
        col=current[1]
        direction=current[2]
        if direction=='N':
            new_row=row-2
            if new_row<0:
                return True
            side=[[new_row,col-1],[new_row,col],[new_row,col+1]]
            for item in side:
                if mat2[item[0]][item[1]]==1:
                    return True
            return False
        elif direction=='S':
            new_row=row+2
            if new_row>19:
                return True
            side=[[new_row,col-1],[new_row,col],[new_row,col+1]]
            for item in side:
                if mat2[item[0]][item[1]]==1:
                    return True
            return False
        elif direction=='E':
            new_col=col+2
            if new_col>14:
                return True
            side=[[row-1,new_col],[row,new_col],[row+1,new_col]]
            for item in side:
                if mat2[item[0]][item[1]]==1:
                    return True
            return False
        else:
            new_col=col-2
            if new_col<0:
                return True
            side=[[row-1,new_col],[row,new_col],[row+1,new_col]]
            for item in side:
                if mat2[item[0]][item[1]]==1:
                    return True
            return False

    def move_forward(self,coordinate,direction):
        r=coordinate[0]
        c=coordinate[1]
        if direction=='N':
            pos=[r-1,c,direction]
        elif direction=='S':
            pos=[r+1,c,direction]
        elif direction=='E':
            pos=[r,c+1,direction]
        else:
            pos=[r,c-1,direction]
        return pos

    def update_direction(self,direction,turn):
        if direction=='N':
            if turn=='L':
                new_direction='W'
            else:
                new_direction='E'
        elif direction=='S':
            if turn=='L':
                new_direction='E'
            else:
                new_direction='W'
        elif direction=='E':
            if turn=='L':
                new_direction='N'
            else:
                new_direction='S'
        else: 
            if turn=='L':
                new_direction='S'
            else:
                new_direction='N'
        return new_direction

    # def left_wall_hug(self,current,mat2):
    #     row=current[0]
    #     col=current[1]
    #     coordinate=[row,col]
    #     direction=current[3]
    #     turned_left=False
    #     response=None
    #     if turned_left==True and self.mat_check_front(current, mat2)==False:
    #         while response==None:
    #             # send move forward 
    #             # check for response
    #         coordinate=self.move_forward(current,direction)
    #         new_direction=direction
    #         turned_left=False

    #     elif self.mat_check_left(current,mat2):
    #         while response==None:
    #             # send direction to turn left
    #             # check for response if response is none continue to send           
    #         new_direction=self.update_direction(direction,'L')
    #         turned_left=True
    #     elif self.mat_check_front(coordinate,direction,mat2)==False:
    #         while response==None:
    #             # send instruction to move front
    #             # check for response if response is none continue to send
    #         coordinate=self.move_forward(coordinate,direction)
    #         new_direction=direction
    #         turned_left=False
    #     else:
    #         while response==None:
    #             # send instruction to turn right
    #             # check for reponse if response is none continue to send  

    #         new_direction=self.update_direction(direction,'R')
    #         turned_left=False           
    #     res=[coordinate[0],coordinate[1],new_direction,turned_left]
    #     return res  
    def explore_remaining(self, current, mat2):
        for i in range(len(mat2)):
            for j in range(len(mat2[0])):
                if mat2[i][j]==3:

                    pos=[i,j]
                    getNeighbours=self.get_valid_surrounding(pos,mat2)
                    if not getNeighbours:
                        continue
                    else:
                        path=self.check_path(current,getNeighbours,mat2)
                        if not path:
                            continue
                        else:
                            return path,pos
        return [],pos
    def get_neighbours(self,coordinate):
        row=coordinate[0]
        col=coordinate[1]
        res=[]
        for i in range(row-2,row+3):
            for j in range(col-2,col+3):
                if (i==row-2 and j==col-2) or (i==row+2 and j==col-2) or (i==row+2 and j==col+2) or (i==row-2 and j==col+2):
                    continue
                elif i==row-2 or i==row+2:
                    res.append([i,j])
                elif j==col-2 or j==col+2:
                    res.append([i,j])
                else:
                    continue
        return res


    def get_valid_surrounding(self,coordinate,mat2):
        neighbours=self.get_neighbours(coordinate)
        res=[]
        for item in neighbours:
            row=item[0]
            col=item[1]
            if item[0]<1 or item[1]<1 or item[0]>18 or item[1]>13:
                continue
            else:
                for i in range(row-1,row+2):
                    for j in range(col-1,col+2):
                        if mat2[i][j]==1 or mat2[i][j]==3:
                            continue
            res.append(item)
        return res

    def check_path(self,coordinate,neighbours,mat2):
        path=[]
        for item in neighbours:
            path=self.bfs(coordinate,item,mat2)
            if not path:
                continue
            else:
                break
        return path

    def bfs(self,start,destination,mat2):
        queue=[[start]]
        path=[]
        visited=set()
        while queue:
            current_path=queue.pop(0)
            current=current_path[-1]
            pos=[current[0],current[1]]
            if tuple(pos)==tuple(destination):
                path=current_path
                break
            neighbours=self.bfs_getNeighbour(pos)
            valid_neighbours=self.bfs_check_neighbours(neighbours,mat2)
            for item in valid_neighbours:
                if tuple([item[0],item[1]]) not in visited:
                    visited.add(tuple([item[0],item[1]]))
                    temp=current_path.copy()
                    temp.append(item)
                    queue.append(temp)
        return path



    def bfs_getNeighbour(self,current):
        row=current[0]
        col=current[1]
        Neighbours=[[row-1,col,'N'],[row+1,col,'S'],[row,col-1,'W'],[row,col+1,'E']]
        return Neighbours
    
    def bfs_check_neighbours(self,neighbours,mat2):
        res=[]
        for item in neighbours:
            valid=True
            row=item[0]
            col=item[1]
            if row<1 or col<1 or row>18 or col>13:
                continue
            else:
                for i in range(row-1,row+2):
                    for j in range(col-1,col+2):
                        if mat2[i][j]==1 or mat2[i][j]==3:
                            valid=False
                            break
                if valid==True:
                    res.append(item)
        return res

    def get_moves(self,current,next):
        d1=current[2]
        d2=next[2]
        path=[]
        if d1==d2:
            path.append('F')
        elif (d1=='N' and d2=='E') or (d1=='E' and d2=='S') or (d1=='S' and d2=='W') or (d1=='W' and d2=='N') :
            path.append('R')
            path.append('F')
        elif (d1=='N' and d2=='W') or (d1=='E' and d2=='N') or (d1=='S' and d2=='E') or (d1=='W' and d2=='S'):  
            path.append('L')
            path.append('F')
        elif (d1=='N' and d2=='S') or (d2=='S' and d1=='N') or (d1=='W' and d2=='E') or (d1=='E' and d2=='W'):
            path.append('R')
            path.append('R')
            path.append('F')
        return path   



    def update_movements_based_on_path(self,path):
        res=[]
        for i in range(1,len(path)):
            moves=self.get_moves(path[i-1],path[i])
            res=res+moves
        return res

    def display_path(self, start, paths,mat2,ROWS,COLS,SIZE,WIN):

        simulate=Simulator_Exploration()
        current=start
        print(paths)
        for item in paths:
            response=False
            if item=='F':
                while not response:
                    break
                    
                    # send movement to move forward
                    # check whether received or not
                current=self.move_forward(current[:2],current[2])
            else:
                while not response:
                    break
                    # send movement to move turn
                    # check whether received or not
                direction=self.update_direction(current[2],item)
                current=[current[0],current[1],direction]
            print(current)      
            simulate.update_map(ROWS,COLS,SIZE,mat2,current[:2],current[2],WIN)
            pygame.display.update()
            pygame.time.wait(500)
            print(item)

    def update_and_display(self,current,turn):
        current_d=current[2]
        new_direction=self.update_direction(current_d,turn)
        pos=[current[0],current[1],new_direction]      
        return pos     

    def adjust_position(self,current,destination,ROWS,COLS,SIZE,mat2,WIN):
        simulate=Simulator_Exploration()
        direction=current[2]
        row=current[0]
        col=current[1]
        pos=current
        # on top of the destination #
        response=False
        if row<destination[0] and destination[0]-row==2:
            if direction=='N':
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break
                pos=self.update_and_display(current,'R')
                print("R")                    
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
                response=False
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break                    
                pos=self.update_and_display(pos,'R')                    
                print("R")
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)         
            elif direction=='W':
                while not response:
                    #send message to turn left
                    #wait for reply
                    response=True
                    break  
                pos=self.update_and_display(current,'L')
                print("L")                    
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
            elif direction=='E':
                while not response:
                    #send message to turn left
                    #wait for reply
                    response=True
                    break  
                pos=self.update_and_display(current,'R')
                print("R")                    
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
        # under the destination
        elif row>destination[0] and row-destination[0]==2:
            if direction=='S':
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break
                pos=self.update_and_display(current,'R')                    
                print("R")
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
                response=False
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break                    
                pos=self.update_and_display(pos,'R')                    
                print("R")
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
            elif direction=='W':
                while not response:
                    #send message to turn right
                    #wait for reply
                    response=True
                    break  
                pos=self.update_and_display(current,'R')
                print("R")                    
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
            elif direction=='E':
                while not response:
                    #send message to turn left
                    #wait for reply
                    response=True
                    break  
                pos=self.update_and_display(current,'L')
                print("L")                    
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
        # to the left of the destination
        elif col<destination[1] and destination[1]-col==2:
            if direction=='W':
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break
                pos=self.update_and_display(current,'R')     
                print("R")               
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
                response=False
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break                    
                pos=self.update_and_display(pos,'R')
                print("R")                    
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)

            elif direction=='N':
                while not response:
                    #send message to turn right
                    #wait for reply
                    response=True
                    break  
                pos=self.update_and_display(current,'R')   
                print("R")                 
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
            elif direction=='S':
                while not response:
                    #send message to turn right
                    #wait for reply
                    response=True
                    break  
                pos=self.update_and_display(current,'L')  
                print("L")                  
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)

        elif col>destination[1] and col-destination[1]==2:
            if direction=='E':
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break
                pos=self.update_and_display(current,'R')      
                print("R")              
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
                response=False
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break                    
                pos=self.update_and_display(pos,'R')        
                print("R")            
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
            elif direction=='N':
                while not response:
                    # send message to turn left
                    # wait for reply
                    response=True
                    break
                pos=self.update_and_display(current,'L')   
                print("L")                 
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
            elif direction=='S':
                while not response:
                    # send message to turn right
                    # wait for reply
                    response=True
                    break
                pos=self.update_and_display(current,'R')                    
                simulate.update_map(ROWS,COLS,SIZE,mat2,pos[:2],pos[2],WIN)
                pygame.display.update()
                pygame.time.wait(300)
        return pos



    def bfs_exploration(self,current,mat1,mat2,ROWS,COLS,SIZE,WIN):
        exp=Exploration_simulation()
        while not self.check_fully_explored(mat2):
            path,destination=self.explore_remaining(current,mat2)
            temp=path[-1]
            print(path)
            path=self.update_movements_based_on_path(path)
            print(path)
            self.display_path(current,path,mat2,ROWS,COLS,SIZE,WIN)
            current=self.adjust_position(temp,destination,ROWS,COLS,SIZE,mat2,WIN)
            exp.update_explored(current[:2],current[2],mat1,mat2)
            pygame.display.update()
            pygame.time.wait(500)
            print("current",current)
            for i in mat2:
                print(i)
        return current  
    # remove mat1 use different sense
    def return_to_start(self,current,mat1,mat2,ROWS,COLS,SIZE,WIN):
        start=[18,1]
        path=self.bfs(current,start,mat2)
        path=self.update_movements_based_on_path(path)
        self.display_path(current,path,mat2,ROWS,COLS,SIZE,WIN)
    # def main_left_wall_hugging(self, current, mat2, size, COLS,ROWS):
    #     traversed_end=False
    #     end=[1,13]
    #     coors=[current[0],current[1]]
    #     temp=coors
    #     simulate=Simulator_Exploration()
    #     
    #     while not traversed_end and current!=temp:
    #         received=False
    #         if tuple(coors)==tuple(end):
    #             traversed_end=True
    #         while not received:
    #             comms.send("Sense")
    #             message=comms.receive()
    #             if message==None:
    #                 continue
    #             else:
    #                 received=True
    #         self.update_map(current,message,mat2)
    #         simulate.update_map(ROWS,COLS,size,mat2,coors,current[2])
    #         pygame.display.update()
    #         pygame.time.wait(300)
    #         current=self.left_wall_hug(current,mat2)
    #         coors=[current[0],current[1]]
    #         simulate.update_map(ROWS,COLS,size,mat2,coors,current[2])
    #         pygame.display.update()
    #         pygame.time.wait(300)
    #    return current
    



        







    

                

