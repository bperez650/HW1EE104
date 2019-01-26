######################################################################
#    Reads in a txt file with values and converts it into matrix     #
#    Computes inverse of matrix and stores both into another file    #                   #
######################################################################



import numpy as np

#---------------------------------------------
#read in file and turn into matrix

with open("hw3_3.txt","r") as readFile:
    size = int(readFile.readline())
    array = []
    for line in readFile:
        array.append(float(line))
    npArray = np.array(array)
    matrix = np.reshape(npArray,(size,size))

#---------------------------------------------
#store matrix in file
    strMatrix = str(matrix)
    with open("HW3_answer.txt","w") as writeFile:
        for element in strMatrix:
            writeFile.write(element)

#---------------------------------------------
#compute inverse of maxtrix and store back in file

        invMatrix = np.linalg.inv(matrix)
        # mul = np.matmul(matrix,invMatrix)   #checking for identity matrix using matrix multipication
        strInvMatrix = str(invMatrix)
        writeFile.write("\n\n")
        for element in strInvMatrix:
            writeFile.write(element)






