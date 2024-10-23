import numpy as np
import random 

print("Enter size of a square matrix")
size = int(input())

matrix = np.eye((size)) 

upperTriangleSum = 0
lowerTriangleSum = 0

for i in range(size):
    for j in range(size):
        matrix[i][j] = random.randint(1,35)

for i in range(size):
    for j in range(size):
        if(i < j):
            upperTriangleSum += matrix[i][j]
        if(i > j):
            lowerTriangleSum += matrix[i][j]

print(upperTriangleSum)
print(lowerTriangleSum)
print(matrix)

