import numpy as np

def populate_array(x_max, y_max, z_max, branch):
        a=np.zeros((x_max, y_max, z_max))
        for i in branch:
                for j in i:
                   a[j[0], j[1], j[2]]=1
        return a

def return_xyz(branch):
        x=np.array([])
        y=np.array([])
        z=np.array([])
        for i in branch:
                for j in i:
                        x=np.insert(x, len(x), j[0])
                        y=np.insert(y, len(y), j[1])
                        z=np.insert(z, len(z), j[2])
        return (x, y, z)


