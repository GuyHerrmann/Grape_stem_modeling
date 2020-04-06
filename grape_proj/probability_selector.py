import random


def num_sel(x,y,z):
    x=x/4.0
    y=y/4.0
    prob=[x, x,x,x, y, y, y, y, z]
    rand=random.random()
    for i in range(0,len(prob)):
        if (rand< prob[i]):
            return i
        else:
            prob[i+1]= prob[i+1]+prob[i]
    return 0
    
def prob_sel(last_num, x, y, z):
    while(1):
        ran_num=num_sel(x, y, z)
        if ran_num==8:
            return ran_num
        elif ran_num%4 != last_num %4:
            return ran_num


def num_sel2(a, b, c):
    rand=random.random()
    prob=[a, b, c]
    for i in range(0,len(prob)):
        if (rand< prob[i]):
            return i
        else:
            prob[i+1]= prob[i+1]+prob[i]
    return 0



