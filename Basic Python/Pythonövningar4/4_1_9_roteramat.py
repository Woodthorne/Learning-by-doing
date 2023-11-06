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
matrix_length = int(input('Mata in matrisens längd: '))     #   These rows contain a method to generate a matrix
matrix = []                                                 #   of a user-determined length per side and filling
for length in range(matrix_length):                         #   it with random double-digit integers.
    row = []                                                #
    for columns in range(matrix_length):                    #   Make sure that they are all commented or not.
        row.append(random.randint(11,99))                   #
    matrix.append(row)                                      #
for row in matrix:
    print(row)

# Checks if the matrix is a quadratic matrix, quits if not
for row in range(len(matrix)-1):
    if len(matrix) != len(matrix[row]):
        print('Detta är inte en matris')
        quit()

# Rotates the matrix clockwise by switching four diagonally symetrical indexes at a time
for depth in range(len(matrix) // 2):
    for step in range(depth,(len(matrix) - 1) - depth):
        matrix[depth][depth+step], matrix[depth+step][-1-depth], matrix[-1-depth][-1-step-depth], matrix[-1-step-depth][depth] = matrix[-1-step-depth][depth], matrix[depth][step+depth], matrix[step+depth][-1-depth], matrix[-1-depth][-1-step-depth]
        # for row in matrix:
        #     print('====',end='')
        # print()
        # for row in matrix:
        #     print(row)

# Prints the rotated matrix with a nice top border
for row in matrix:
    print('====',end='')
print()
for row in matrix:
    print(row)