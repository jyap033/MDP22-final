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
        print(new_mov)
        return new_mov
hex=hex="000000000000010042038400000000000000030C000000000000021F8400080000000000040"
waypoint=[3,2]
sol=AlgorithmManager()
movs=sol.compute(hex,waypoint)
print(movs)
