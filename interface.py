import numpy as np


def num_inputs(string, rang):
    while(1):
        try:
            a=int(raw_input(string))
        except ValueError:
            print("Invalid Input")
        else:
            if (a<rang[1] and a>rang[0]):
                return a
            else:
                print("Input out of range")
    

def read_inputs():
    g = num_inputs("Grapes? (1 for present, 0 for not): ", [-1, 2])
    leng= num_inputs('Height (1 to 15):', [0, 16])
    sigma_F= num_inputs('Randomness in branch length (0 to 10): ', [-1, 11])
    sigma_an= num_inputs('Randomness in branch angles (0,10: )', [-1,11])
    angle= np.radians(num_inputs('Branching angle (45 to 90): ', [44, 91]))
    size= num_inputs('Size (100 to 1000):', [99, 1001])
    return (g, leng, sigma_an, sigma_F, angle, size)    
