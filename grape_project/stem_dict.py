###File storing dictionaries used in
#Grape stem modeling project

#General dictionary to convert Symbol to itself
gen_dict={'F': 'F', '-': '-', '+': '+', '[': '[', ']': ']', '&': '&', '|': '|',
          '^': '^', '~': '~', '?': '?', '!': '!', 'H': 'H'}
# Dictionary to select probablity distributions
prob_dict={0: 0 , 1: 0.0, 2: 0.00, 3:0 , 4: 0 , 5:0.05 , 6:0.1 , 7:0.15, 8: 0.2, 9: 0.3, 10: 0.3} 
#transformations for the symbol C if iterated through
gen_c1={0: '[?FH]', 1: '[~FH]', 2:'[&FH]', 3:'[^FH]', 4: '[?FA]', 5: '[~FA]', 6:'[&FB]', 7:'[^FB]', 8:''}
gen_c2={0: 'C', 1: 'FC', 2: ''}

#Transformations for the symbol A if iterated through
gen_a1={0: '[+FH]', 1: '[-FH]', 2: '[~FH]', 3: '[?FH]',4: '[+FB]', 5: '[-FB]', 6: '[~FC]', 7: '[?FC]', 8: ''}
gen_a2={0: 'A', 1: 'FA', 2: ''}

#Transformations for the symbol B if iterated though
gen_b1={0: '[+FH]', 1: '[-FH]', 2: '[&FH]', 3: '[^FH]', 4: '[+FA]', 5: '[-FA]', 6: '[&FC]', 7: '[^FC]', 8: ''}
gen_b2={0: 'B', 1: 'FB', 2: ''}

#two are included for each transformation to add to randomness in the program
