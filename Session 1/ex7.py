import numpy as np

# Creating two 3x3 matrices
A = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

B = np.array([[9, 8, 7], 
              [6, 5, 4], 
              [3, 2, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix Addition
C = A + B
print("\nMatrix Addition:\n", C)

# Matrix Subtraction
D = A - B
print("\nMatrix Subtraction:\n", D)

# Matrix Multiplication (Dot Product)
E = np.dot(A, B)
print("\nMatrix Multiplication (Dot Product):\n", E)

# Transpose of a Matrix
A_T = A.T
print("\nTranspose of A:\n", A_T)

# Determinant of Matrix A
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)

# Identity Matrix (3x3)
I = np.eye(3)
print("\nIdentity Matrix:\n", I)
