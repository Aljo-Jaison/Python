import numpy as np

matrix_A = np.random.randint(0, 21, (3, 3))
matrix_B = np.random.randint(0, 21, (3, 3))

matrix_sum = matrix_A + matrix_B

matrix_product = np.dot(matrix_A, matrix_B)

matrix_transpose = matrix_product.T

print("Matrix A:\n", matrix_A)
print("\nMatrix B:\n", matrix_B)
print("\nMatrix Addition (A + B):\n", matrix_sum)
print("\nMatrix Multiplication (A * B):\n", matrix_product)
print("\nTransposed Product Matrix:\n", matrix_transpose)
