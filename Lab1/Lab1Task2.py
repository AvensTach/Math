import numpy as np

# task: A * X * B = C, find matrix X

A = np.array([[5, 4],
              [9, 7]])

B = np.array([[7, 8, 7],
              [8, 9, 6],
              [5, 6, 8]])

C = np.array([[-1, -1, 0],
              [1, 1, 0]])

A_inv = np.linalg.inv(A)

B_inv = np.linalg.inv(B)

X = A_inv @ C @ B_inv

X_dot = np.dot(A_inv, C)
X_dot = np.dot(X_dot, B_inv)

print("Matrix X:")
print(X)
print("np.dot method:")
print(X_dot)
