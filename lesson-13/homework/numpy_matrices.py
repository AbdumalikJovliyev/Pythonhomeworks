import numpy as np
# 1. Create a vector with values ranging from 10 to 49.

vector=np.arange(10,50)
print("\n1.Vector created by arange:\n ", vector)

# 2. Create a 3x3 matrix with values ranging from 0 to 8.

matrix = np.arange(9).reshape(3, 3)
print("\n2.3x3 matrix: \n",matrix)

# 3. Create a 3x3 identity matrix.

matrix=np.identity(3, dtype=int)
print("\n3. Identity matrix: ", matrix)

# 4. Create a 3x3x3 array with random values.

array_3x3x3 = np.random.random((3, 3, 3))
print("\n4.3D matrix with random values:\n", array_3x3x3)

# 5. Create a 10x10 array with random values and find the minimum and maximum values.

array_10=np.random.randint(1,11,(10,10))
print("\n5. Max_min \n", array_10)
print("Max: ", array_10.max())
print("Min: ", array_10.min())

# 6. Create a random vector of size 30 and find the mean value.

vect=np.random.randint(30)
print("\n6. Mean value: ", np.mean(vect))

# 7. Normalize a 5x5 random matrix.

random_vector = np.random.random((5,5))
normalized_vector = random_vector / np.linalg.norm(random_vector)
print("\n7.vector normalize. \nOriginal Vector: \n", random_vector)
print("Normalized Vector:\n", normalized_vector)

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).

matrix_5=np.random.randint(1,15,(5,3))
matrix_2=np.random.randint(1,6,(3,2))
print("\n8. Matrix product: \n", matrix_5.dot(matrix_2))    

# 9. Create two 3x3 matrices and compute their dot product.

matrix_a = np.random.randint(1, 10, (3, 3))
matrix_b = np.random.randint(1, 10, (3, 3))
result_9 = np.dot(matrix_a, matrix_b)
print("\n9. Dot product: \n", result_9)

# 10. Given a 4x4 matrix, find its transpose.

matrix_4x4 = np.random.randint(1, 10, (4, 4))
transpose_10 = matrix_4x4.transpose()
print("\n10. Transpose of a 4x4 matrix:")
print(transpose_10)

# 11. Create a 3x3 matrix and calculate its determinant.

matrix_3x3 = np.random.randint(1, 10, (3, 3))
determinant_11 = np.linalg.det(matrix_3x3)
print("\n11. Determinant of a 3x3 matrix:")
print(determinant_11)

# 12. Create two matrices A (3x4) and B (4x3), and compute the matrix product A · B.

matrix_a_3x4 = np.random.randint(1, 10, (3, 4))
matrix_b_4x3 = np.random.randint(1, 10, (4, 3))
result_12 = np.dot(matrix_a_3x4, matrix_b_4x3)
print("\n12. Matrix product of A (3x4) and B (4x3):")
print(result_12)

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.

matrix_3x3 = np.random.randint(1, 10, (3, 3))
vector_3 = np.random.randint(1, 10, (3, 1))
result_13 = np.dot(matrix_3x3, vector_3)
print("\n13. Matrix-vector product of a 3x3 matrix and a 3-element column vector:")
print(result_13)

# 14. Solve the linear system Ax = b where A is a 3x3 matrix, and b is a 3x1 column vector.

A = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 1))
x = np.linalg.solve(A, b) 
print("Solution x:")
print(x)

# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.

matrix_5x5 = np.random.randint(1, 10, (5, 5))
row_sums = np.sum(matrix_5x5, axis=1)
column_sums = np.sum(matrix_5x5, axis=0)
print("\n15. Row-wise and column-wise sums of a 5x5 matrix:")
print("Row-wise sums:")
print(row_sums)
print("Column-wise sums:")
print(column_sums)