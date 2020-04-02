from probability_selector import *
from stem_dict import *

def gen(Lsys, count):
    a, b, c= (0.4, 0.5, 0.2)
    x_r, y_r, z= (0.6, 0.4, 0.0)
    st=''
    count=count-1
    ran_num1=0
    ran_num3=0
    ran_num2=0
    m_node_count=-1
    layer=0
    if count>0:
        for i in Lsys:
            if i == 'B':                                
                ran_num1=prob_sel(ran_num1, x, y, z)
                st+= gen_b1[ran_num1]
                st+= gen_b2[num_sel2(a,b,c)]# Nah, this shouldn't just be random But can wrk on!
            elif i =='A':
                ran_num2=prob_sel(ran_num2, x, y, z)
                st+= gen_a1[ran_num2]
                st+=gen_a2[num_sel2(a, b ,c)]
            elif i=='C':
                ran_num3=prob_sel(ran_num3, x, y, z)
                st+= gen_c1[ran_num3]
                if layer==0:
                    st+=gen_c2[num_sel2(0,0,1)]
                else:
                    st+= gen_c2[num_sel2(a, b, c)]
            elif i=='[':
                layer=layer+1
                st+=i
            elif i==']':
                layer= layer-1
                st+=i
            elif i=='F':
                if (layer==0):
                    m_node_count= m_node_count+1
                    if m_node_count<11:
                        x= x_r+prob_dict[m_node_count]
                        y=y_r-prob_dict[m_node_count]    
                st+=i
            else:
                st+= i
        return gen(st, count)
    if count==0:
	    return Lsys
