from queue import PriorityQueue
from Map import Preprocess_Map
class A_star:
    def check_obstacles(self,pos,matrix):
        if matrix[pos[0]][pos[1]]==1:
            return True
        else:
            return False

    def getNeighbours(self,pos, matrix):
        top=[pos[0]-1,pos[1]]
        down=[pos[0]+1,pos[1]]
        left=[pos[0],pos[1]-1]
        right=[pos[0],pos[1]+1]
        neighbors=[top,down,left,right]
        res=[]
        for item in neighbors:
            if item[0]<=0 or item[1]<=0 or item[0]>=len(matrix)-1 or item[1]>=len(matrix[0])-1:
                continue
            elif not self.check_obstacles(item, matrix):
                res.append(tuple(item))
        return res
    def getDirections(self, current, neighbour, direction):
        c_row=current[0]
        c_col=current[1]
        n_row=neighbour[0]
        n_col=neighbour[1]
        if direction=="N":
            if n_row-c_row==-1:
                return "N",0
            elif n_row-c_row==1:
                return "S",8
            elif n_col-c_col==1:
                return "E",4
            else:
                return "W",4
        elif direction=="S":
            if n_row-c_row==-1:
                return "N",8
            elif n_row-c_row==1:
                return "S",0
            elif n_col-c_col==1:
                return "E",4
            else:
                return "W",4
        elif direction=="W":
            if n_row-c_row==-1:
                return "N",4
            elif n_row-c_row==1:
                return "S",4
            elif n_col-c_col==1:
                return "E",8
            else:
                return "W",0
        else:
            if n_row-c_row==-1:
                return "N",4
            elif n_row-c_row==1:
                return "S",4
            elif n_col-c_col==1:
                return "E",0
            else:
                return "W",8

    def calculate_h(self, item, end):
        vertical=abs(end[0]-item[0])
        horizontal=abs(end[1]-item[1])
        return vertical + horizontal

    def construct_path(self, came_from, current):
        L1=[]
        L2=[]
        while current in came_from:
            current=came_from[current]
            L1.append(current[0])
            L2.append(current[1])
        return L1,L2
    
        
    def A_star(self, matrix,end,start,dir):
        count=0
        start=tuple(start)
        open_set=PriorityQueue()
        open_set.put((0,count,start,dir))
        came_from={}
        g_score={}
        f_score={}
        row= len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for j in range(col):
                g_score[tuple([i,j])]=float("inf")
                f_score[tuple([i,j])]=float("inf")
        # start position should have only h_score, so we can set its F to H

        g_score[start]=0
        f_score[start]=self.calculate_h(start,end)
        open_set_hash={start}
        while not open_set.empty():
            now=open_set.get()
            current=now[2]
            print(current)
            direction=now[3]
            current_and_dir=(current,direction)
            if current==end:
                res, dirs=self.construct_path(came_from,current_and_dir)
                res.reverse()
                res.append(end)
                dirs.reverse()
                dirs.append(direction)
                return res, dirs
            for neighbour in self.getNeighbours(current,matrix):
                neighbour_dir, turn = self.getDirections(current, neighbour,direction)
                temp_g=g_score[current]+1+turn
                if temp_g< g_score[neighbour]:
                    came_from[(neighbour,neighbour_dir)]=current_and_dir
                    g_score[neighbour]=temp_g

                    f_score[neighbour]=temp_g + self.calculate_h(neighbour,end)
                    if neighbour not in open_set_hash:
                        count+=1
                        open_set.put((f_score[neighbour],count,neighbour,neighbour_dir))
                        open_set_hash.add((neighbour,neighbour_dir))
        return [],[]

    def get_path(self, hex, mid_point):
        Bin=Preprocess_Map.hex_to_bin(self,hex)
        matrix1=Preprocess_Map.bin_to_matrix(self,Bin)
        for i in matrix1:
            print(i)
        temp_matrix=Preprocess_Map.add_walls(self,matrix1)
        for i in temp_matrix:
            print(i)
        start=[1,1]
        mid=tuple(mid_point)
        path1,dir1=self.A_star(temp_matrix,mid,start,"S")
        print(path1)
        print(dir1)
        direction=dir1[-1]
        end=tuple([18,13])
        path2,dir2=self.A_star(temp_matrix,end,mid_point,direction)
        dir2=dir2[1:]
        dir=dir1+dir2
        return path1, path2, dir
    def process_directions(self,dir):
        mov=[]
        for i in range(1,len(dir)):
            if dir[i]==dir[i-1]:
                mov.append("F")
            else:
                if (dir[i]=="E" and dir[i-1]=="N") or (dir[i]=="N" and dir[i-1]=="W") or (dir[i]=="W" and dir[i-1]=="S") or (dir[i]=="S" and dir[i-1]=="E"):
                    mov.append("R")
                    mov.append("F")
                elif (dir[i]=="E" and dir[i-1]=="S") or (dir[i]=="N" and dir[i-1]=="E") or (dir[i]=="W" and dir[i-1]=="N") or (dir[i]=="S" and dir[i-1]=="W"):
                    mov.append("L")
                    mov.append("F")
                else:
                    mov.append("Reverse")
                    mov.append("F")
        return mov

    def process_mov(self,mov):
        count=0
        temp=None
        res=[]
        for i in range(len(mov)):
            if mov[i]!=temp and temp==None:
                temp=mov[i]
                count+=1
            elif i==len(mov)-1 and mov[i]==temp:
                print(temp,i)
                count+=1
                res.append(temp+str(count))
            elif i==len(mov)-1 and mov[i]!=temp:
                res.append(temp+str(count))
                res.append(mov[i]+str(1))
            elif mov[i]!=temp:
                res.append(temp+str(count))
                temp=mov[i]
                count=1
            else:
                count+=1
        return res
     def process2(self, movs):
        for i in range(len(movs)):
            if movs[i]=="Reverse1":
                movs[i]="R2"

    def process3(self, movs):
        res=[]
        for item in movs:
            temp=[item[0]]*int(item[1:])
            res+=temp
        return res
        
