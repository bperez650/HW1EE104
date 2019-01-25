#########################################################
#                                                       #
# Will work for files with only numbers and dashes,     #
# files with alpha chars will fail                      #
#########################################################

import numpy as np

sum = 0 #variable for sum of squares
index = 0   #index so we can take average

with open("hw2_3.txt","r") as file:

    for line in file:   #loop over all lines in file
        cast = float(line)  #parse out numerical characters and cast into floats
        sum += cast**2
        index  += 1

    sum /= index
    total = np.sqrt(sum)
    print(total)




