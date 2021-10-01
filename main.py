import matrix_functions
import random

# A random matrix is going to be generated
n_rows = random.randint(2,5)
n_colums = random.randint(2,5)

numbers = list()
row = list() 

for i in range(n_rows):
    for j in range(n_colums):
        row.append(random.randint(0,10))
    numbers.append(row)
    row = []

# Prints the matrix generated
print("Original:")
for row in numbers:
    print(row)

transposed = matrix_functions.transpose(numbers)
print("\n"+"Transpose:")
for row in transposed:
    print(row)

