from Map import Preprocess_Map
from Shortest_path import A_star

class AlgorithmManager:
    def compute(self,hex,mid_point):
            
        sol=A_star()
        p1,p2,dir=sol.get_path(hex,mid_point)
        path=p1+p2[1:]

        for i in range(len(dir)):
            if dir[i]=="N":
                dir[i]="S"
            elif dir[i]=="S":       
                dir[i]="N"
            else:
                continue
        pre=Preprocess_Map()
        mat=pre.generate_path(hex,path)
        for i in mat:
            print(i)
        movements=sol.process_directions(dir)
        print(movements)
        new_mov=sol.process_mov(movements)
        sol.process2(new_mov)
        return new_mov
hex="0700000000000001C00002000400080010202040408001000200040000380000000020004200"
waypoint=[2,3]
sol=AlgorithmManager()
movs=sol.compute(hex,waypoint)
print(movs)
