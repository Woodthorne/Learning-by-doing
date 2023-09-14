# The assignment was to make a program that rotates a matrix
# by 90 degrees clockwise without copying or making a new
# matrix. After showing this to a friend who works in
# programming he pointed out it can just as easily be done
# with a zip()-function. All in all this took about an hour
# to do and I'm still quite proud of figuring out how to do
# it, even if it's easily replaced by a core function.

import random

# Determines the matrix and prints it
# matrix = [[11,12],
#           [21,22]]
# matrix = [[11,12,13],
#           [21,22,23],
#           [31,32,33]]
# matrix = [[11,12,13,14],
#           [21,22,23,24],
#           [31,32,33,34],
#           [41,42,43,44]]
# matrix = [[11,12,13,14,15],
#           [21,22,23,24,25],
#           [31,32,33,34,35],
#           [41,42,43,44,45],
#           [51,52,53,54,55]]
matrix_length = int(input('Input the desired matrix length: ')) #   These rows contain a method to generate a matrix
matrix = []                                                     #   of a user-determined length per side and filling
for length in range(matrix_length):                             #   it with random double-digit integers.
    row = []                                                    #
    for columns in range(matrix_length):                        #   Make sure that they are all either commented or
        row.append(random.randint(11,99))                       #   part of the code together.
    matrix.append(row)                                          #
for row in matrix:
    print(row)

# Checks if the matrix is a quadratic matrix, quits if not
for row in range(len(matrix)-1):
    if len(matrix) != len(matrix[row]):
        print('This is not a quadratic matrix.')
        quit()

# Rotates the matrix clockwise by switching four diagonally symetrical indexes at a time
for depth in range(len(matrix) // 2):
    for step in range(depth,(len(matrix) - 1) - depth):
        matrix[depth][depth+step], matrix[depth+step][-1-depth], matrix[-1-depth][-1-step-depth], matrix[-1-step-depth][depth] = matrix[-1-step-depth][depth], matrix[depth][step+depth], matrix[step+depth][-1-depth], matrix[-1-depth][-1-step-depth]
        # for row in matrix:        # 
        #     print('====',end='')  #
        # print()                   # Optional bit of code to see the rotation step-by-step.
        # for row in matrix:        # (Copy of the print code below)
        #     print(row)            #

# Prints the rotated matrix with a nice top border
for row in matrix:
    print('====',end='')
print()
for row in matrix:
    print(row)