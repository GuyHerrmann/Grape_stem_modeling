import numpy as np
import pandas as pd
def collision_detector(bran, size):
        a=np.array(bran[0])
        for i in range(1,len(bran)):
                b=np.array(bran[i][0:])
                a=np.concatenate((a,b))
        del_bran=[]
        df1=pd.DataFrame(a)
        df1=df1.sort_values([0,1,2], ascending= [True, True, True])
        df= df1.values
        
        count=0
        count1=0
        counth=0
        for i in range (1, df[:, 0].size):  
                #Array Indexes for i: 0= x_coord, 1= y_coord, 2= z_coord, 3= Layer, 4=index for deletion, 5=Bra_0, 6=Bra_1
                if (df[i][5]==df[i-1][5]):              # Tests if on same branch
                        if (abs(df[i][3]-df[i-1][3])>1) and (df[i][3]==3 or df[i-1][3] == 3) and (df[i][5]!=0):
                #If: difference of 2 or more in layers, either on third layer, Neither on 0th Branch (can
                                if df[i][6]!=df[i-1][6]:                #Ensures not on same tertiary Branch
                                        if (np.linalg.norm(df[i][:3]-df[i-1][:3])<(size/20)):#Tests if coordinates are within given distance
                                                count1=count1+1
                                                if (df[i][3]>df[i-1][3]):
                                                        del_bran.insert(len(del_bran), df[i])
                                                elif (df[i][3]<df[i-1][3]):
                                                        del_bran.insert(len(del_bran), df[i-1])
                                                else:
                                                        del_bran.insert(len(del_bran), df[i-random.randint(0,1)])
                elif ((df[i][3]==0) and (df[i-1][3]==1)) or ((df[i-1][3]==0)## Case for not on the same Branch!
                                                             and (df[i][3]==1)) or (df[i-1][3]==1 and df[i-1][3]==1):
                        counth=counth+1         # If this is the Case Can't be a colllision!
                else:
                        if(np.linalg.norm(df[i][:3]-df[i-1][:3])< (size/20)):
                                count=count+1#
                                #Below decides which coordinate should be deleted
                                if (df[i][3]>df[i-1][3]):
                                        del_bran.insert(len(del_bran), df[i])
                                elif (df[i][3]<df[i-1][3]):
                                        del_bran.insert(len(del_bran), df[i-1])
                                else:
                                        del_bran.insert(len(del_bran), df[i-random.randint(0,1)])
                                        
                                #Don't DO anything
                        
        if len(del_bran)>0:
                del_bran=np.unique(del_bran, axis=0)

        del_bra_index=[]
        #Below: Decides how to decide which branches t be deleted with deleted branches!
        for i in del_bran:
                if i[3]==1:
                        print("Error, This shoud not happen!")
                elif (i[3]==2):
                        branch= i[6]
                        out=df1[(df1[6]== i[6]) & (df1[5]==i[5]) & (df1[3]>1)][4].values
                        out=np.unique(out, axis=0)
                        for i in out:
                                del_bra_index.insert(len(del_bra_index), i)
                        
                elif (i[3]==3):
                        del_bra_index.insert(len(del_bra_index), i[4])
        del_bra_index=np.unique(np.array(del_bra_index))
        #print(len(del_bra_index))
        return del_bra_index
