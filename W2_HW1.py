import re
import numpy as np

sum_num = 0
numlist = []
file = open('regex_sum_221987.txt', 'r')

for line in file:
    line = line.rstrip()
    number = re.findall('[0-9]+' , line)
    if not number:
        continue
    else:
        for temp in number:
            numlist.append(int(temp))


print(np.sum(numlist))
'''
sum_num = np.sum(numlist)
print(sum_num)
'''


    
