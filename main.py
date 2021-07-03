import matrix_functions
from random import randint as rint

# A random matrix is going to be generated
n_rows = rint(2,5)
n_colums = rint(2,5)

numbers = []
row = []
for i in range(n_rows):
    for j in range(n_colums):
        row.append(rint(0,10))
    numbers.append(row)
    row = []

# Prints the matrix generated
print("Original:", numbers)

tansposed = matrix_functions.transpose(numbers)
print("\n"+"Transpose:", tansposed)
