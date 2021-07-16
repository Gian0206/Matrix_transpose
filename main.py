import matrix_functions
import random

# A random matrix is going to be generated
n_rows = random.randit(2,5)
n_colums = random.randint(2,5)

# numbers = list() *% #Pass for later adding 
# row = list() *% #Pass for later

for i in range(n_rows):
    for j in range(n_colums):
        row.append(rint(0,10))
    numbers.append(row)
    row = []

# Prints the matrix generated
print("Original:", numbers)

tansposed = matrix_functions.transpose(numbers)
print("\n"+"Transpose:", tansposed)
