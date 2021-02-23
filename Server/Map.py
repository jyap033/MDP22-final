
import math 
class Preprocess_Map:
    def hex_to_bin(self, hex):       
        # Initialising hex string 
        ini_string = "1"+hex
        res = "{0:08b}".format(int(ini_string, 16)) 
        n_res=str(res)
        return n_res[1:]
    
    def bin_to_matrix(self, bin):
        matrix=[]
        i=0
        for j in range(20) :
            temp=[]
            while len(temp)<15:
                temp.append(int(bin[i]))
                i+=1
            matrix.append(temp)
        return matrix

        
    def reverse(self, matrix):
        length=len(matrix)
        left=0
        right=length-1
        while left<right:
            matrix[left],matrix[right]=matrix[right],matrix[left]
            left+=1
            right-=1
        return matrix

    def generate_path(self, hex, path):
        binary=self.hex_to_bin(hex)
        matrix=self.bin_to_matrix(binary)
        for i in path:
            matrix[i[0]][i[1]]=3
        act_mat=self.reverse(matrix)
        return act_mat

    def add_walls(self,matrix):
        L1=[]
        matrix1=matrix.copy()
        row=len(matrix1)
        col=len(matrix1[1])
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                if matrix1[i][j]==1:
                    L1.append([i,j])

        for item in L1:
            print(item)
            if item[0]<=2 and item[1]<=2:
                continue
            elif item[0]==0 and item[1]==col-1:
                matrix1[item[0]+1][item[1]]=1
                matrix1[item[0]][item[1]-1]=1
                matrix1[item[0]+1][item[1]-1]=1
            elif item[0]==row-1 and item[1]==0:
                matrix1[item[0]-1][item[1]]=1
                matrix1[item[0]][item[1]+1]=1
                matrix1[item[0]-1][item[1]+1]=1
            elif item[0]==row-1 and item[1]==col-1:
                matrix1[item[0]-1][item[1]]=1
                matrix1[item[0]][item[1]-1]=1
                matrix[item[0]-1][item[1]+1]=1

            elif item[0]==0:
                matrix1[item[0]+1][item[1]]=1
                matrix1[item[0]][item[1]-1]=1
                matrix1[item[0]][item[1]+1]=1
                matrix1[item[0]+1][item[1]-1]=1
                matrix1[item[0]+1][item[1]+1]=1

            elif item[0]==row-1:
                matrix1[item[0]-1][item[1]]=1
                matrix1[item[0]][item[1]-1]=1
                matrix1[item[0]][item[1]+1]=1
                matrix1[item[0]-1][item[1]-1]=1
                matrix1[item[0]-1][item[1]+1]=1
            elif item[1]==0:
                matrix1[item[0]][item[1]+1]=1
                matrix1[item[0]-1][item[1]]=1
                matrix1[item[0]+1][item[1]]=1
                matrix[item[0]-1][item[1]+1]=1
                matrix[item[0]+1][item[1]+1]=1
            elif item[1]==col-1:
                matrix1[item[0]][item[1]-1]=1
                matrix1[item[0]-1][item[1]]=1
                matrix1[item[0]+1][item[1]]=1
                matrix1[item[0]-1][item[1]-1]=1
                matrix1[item[0]+1][item[1]-1]=1

            else:
                matrix1[item[0]][item[1]+1]=1
                matrix1[item[0]][item[1]-1]=1
                matrix1[item[0]-1][item[1]]=1
                matrix1[item[0]+1][item[1]]=1
                matrix1[item[0]-1][item[1]-1]=1
                matrix1[item[0]+1][item[1]-1]=1
                matrix1[item[0]-1][item[1]+1]=1
                matrix1[item[0]+1][item[1]+1]=1
                

        return matrix1



