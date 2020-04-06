
import numpy as np
import math
import random
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import os
from stem_dict import *
from probability_selector import *
from interface import *
from draw_shape import *
from stem_generate import gen
#Excuse the bad syntax of importing all.
from collision_detector import collision_detector
from array_pop import populate_array, return_xyz


if __name__ == '__main__':
    
        g, leng, change_an, change_F, r_an, size= read_inputs()
        g, change_an, change_F, r_an=(0, 2, 2, np.radians(77))  #Should be configurable variables
        x_max, y_max, z_max= (size, size, size)      
        c_cursor=np.array([x_max/2, y_max/2, z_max/8])
        d_cursor=np.array([0,0,1]) 
        t_cursor= size/90
        F_cursor= size/10

        sigma_F=(size/300)*change_F
        sigma_d=(r_an/45)*change_an
        sigma_an=(r_an/45)*change_an
        
        pos=[]
        branches=[]
        grapes= []        
        bra_stor=0
        bra_0=0
        bra_1=0

        yes=1
        
        g_rad=int(size/30+0.5)
        #Setting the axiom
        axiom='F'
        for i in range(0, leng):
            axiom+='C'
            if (random.random()<0.6):
                axiom+='F'
        Lsys=gen(axiom, 8) #Generation of literal sequence
        count_bra=0
        layer=0
        La_count=[0, 0, 0]
        #For loop to scan Literals
        for i in Lsys:
                if i== 'F':
                        #This line_ coord  thing is problematic but okay
                        leng=np.random.normal(F_cursor, sigma_F)
                        #Randomizatin function to randomise the d_cursor direction
                        ran= np.random.randint(0,2)
                        if ran==0:
                                d_cursor= np.dot(d_cursor, Ru(np.random.normal(0, sigma_d)))
                                d_cursor=np.dot(d_cursor, Rl(np.random.normal(0, sigma_d)))
                                d_cursor=np.dot(d_cursor, Rh(np.random.normal(0, sigma_d))) 
                        if ran==1:
                                d_cursor=np.dot(d_cursor, Rl(np.random.normal(0, sigma_d)))                                
                                d_cursor= np.dot(d_cursor, Ru(np.random.normal(0, sigma_d)))
                                d_cursor=np.dot(d_cursor, Rh(np.random.normal(0, sigma_d)))
                        if ran==2:
                                d_cursor=np.dot(d_cursor, Rh(np.random.normal(0, sigma_d)))
                                d_cursor=np.dot(d_cursor, Rl(np.random.normal(0, sigma_d)))                                
                                d_cursor= np.dot(d_cursor, Ru(np.random.normal(0, sigma_d)))

                            #Ensures layer 4 not drawn and no long branch on layer 3
                        if (layer==2):
                            yes=1
                        if (layer<4 and yes==1):
                            (line_coord, c_cursor)=vectcylind((c_cursor+0.5).astype(int), d_cursor, int(t_cursor+0.5), leng, layer, len(branches), bra_0, bra_1)
                            branches.insert(len(branches), line_coord)
                        else:
                            yes=0

                            

                         
                elif i=='-':
                        rot= np.random.normal(r_an, sigma_an)
                        d_cursor=np.dot(d_cursor, Ru(rot))
                        
                elif i=='+':
                        rot= np.random.normal(r_an, sigma_an)
                        d_cursor=np.dot(d_cursor, Ru(-rot))
                        
                elif i=='&':
                        rot= np.random.normal(r_an, sigma_an)
                        d_cursor=np.dot(d_cursor, Rl(rot))
                        
                elif i=='^':
                        rot= np.random.normal(r_an, sigma_an)
                        d_cursor=np.dot(d_cursor, Rl(-rot))
                        
                elif i=='~':
                        rot= np.random.normal(r_an, sigma_an)
                        d_cursor=np.dot(d_cursor, Rh(rot))
                        
                elif i=='?':
                        rot= np.random.normal(r_an, sigma_an)
                        d_cursor=np.dot(d_cursor, Rh(-rot))
                elif i=='|':
                        d_cursor=np.dot(d_cursor, Ru(np.pi))                        
                
                elif i=='[':
                        if layer==0:
                                count_bra=count_bra+1
                                bra_0=bra_stor+1
                                bra_1=0
                        elif layer==1:
                                bra_1=bra_1+1
                                
                                
                        arr=[c_cursor, d_cursor, t_cursor, F_cursor, layer]
                        pos.insert(len(pos), arr)
                        if layer<3:
                            La_count[layer]=0
                        layer= layer+1
                        
                        t_cursor=t_cursor*0.65#Can't really beleive  but not inverse for when back!'
                        if t_cursor<1:
                            t_cursor=1
                        F_cursor=F_cursor*0.85
                        
                elif i==']':
                        if layer==1:    
                                bra_stor=bra_0
                                bra_0=0
                        arr= pos.pop()
                        c_cursor, d_cursor, t_cursor, F_cursor, layer = arr
                        
                elif i=='H':
                    if (g==1):
                        grapes.insert(len(grapes), sphere(c_cursor, d_cursor, g_rad))
                        
        
        #array= populate_array(x_max, y_max, z_max, branches)
        
        collisions= collision_detector(branches, size)
        #print('collisions')
        if (len(collisions)>1):
                j=0
                for i in collisions:
                        del branches[i-j]
                        j=j+1
        #Plots the graph
        (x,y,z)=return_xyz(branches)
        (a, b, c)= return_xyz(grapes)
        fig= plt.figure()
        ax= fig.add_subplot(111, projection='3d')
        ax.set_xlim([0, x_max])    
        ax.set_ylim([0, y_max])
        ax.set_zlim([0,z_max])
        ax.scatter(x, y, z, zdir= 'z', c='brown')
        ax.scatter(a, b, c, zdir='z', c='green')
        plt.axis('off')
        plt.show()
        save=num_inputs("Save plot? (1 : yes, 0: no", [-1, 2])
        if(save==1):

            #Opens file and prints to file
            
            out=populate_array(size, size, size, branches)
            print(out.shape)
            name=raw_input("File Name:")
            file=open(name+ '.txt', "w")
            
            for i in range(out.shape[0]):
                file.write('\n\n')
                for j in range(out.shape[1]):
                    file.write('\n')
                    for k in range(out.shape[2]):
                        file.write(str(int(out[i, j, k]))+ ' ')
            file.close()
