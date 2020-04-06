import numpy as np

def line(init, di, length, layer, bra, bra_0, bra_1):
    final=init+di*length
    pos=init
    pos1=init
    line=np.array([[init[0], init[1], init[2], layer, bra, bra_0, bra_1]])
    for i in range(0, int(length+0.5)):
        pos+= di
        for i in range(3):
            if np.abs(0.5-(pos[i]%1))<0.51:
                ret2=np.ndarray.astype(np.array([[pos[0]+0.5, pos[1]+0.5, pos[2]+0.5, layer, bra, bra_0, bra_1]]), int)
                line=np.concatenate((line, ret2))
    line=np.unique(line, axis=0)
    return line


def vectcylind(init, di, r, length, layer, bra, bra_0, bra_1):
    final = init+length*di
    coord=np.array([[init[0], init[1], init[2], layer, bra, bra_0, bra_1]])
    for x in range(init[0]-r, init[0]+r):
        for y in range(init[1]-r, init[1]+r):
            for z in range(init[2]-r, init[2]+r):
                if ((di[0]*(x-init[0])+di[1]*(y-init[1])+di[2]*(z-init[2])<0.5)and (((init[0]-x)**2+(init[1]-y)**2 +(init[2]-z)**2))<r):
                    out=line([x,y,z], di, length, layer, bra, bra_0, bra_1)
                    coord=np.concatenate((coord, out))
    return (coord, final)

def sphere(pos, d_vector, rad):
        centre= (pos+(d_vector*rad)+0.5).astype(int)
        sphere_coord=np.array([centre])
        for x in range(centre[0]-rad, centre[0]+rad):
                for y in range(centre[1]-rad, centre[1]+rad):
                        for z in range(centre[2]-rad, centre[2]+rad):   
                                if ((x-centre[0])**2+(y-centre[1])**2+(z-centre[2])**2)<rad**2:
                                        sphere_coord=np.concatenate((sphere_coord, [[x,y,z]]))
        return sphere_coord

def Ru(an):
        return np.array([[np.cos(an), np.sin(an), 0],[-np.sin(an), np.cos(an), 0], [0,0,1]])

def Rl(an):
        return np.array([[np.cos(an), 0, -np.sin(an)],[0,1, 0], [np.sin(an), 0, np.cos(an)]])

def Rh(an):
        return np.array([[1, 0, 0], [0, np.cos(an), -np.sin(an)], [0, np.sin(an), np.cos(an)]])
