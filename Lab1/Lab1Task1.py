import sympy as sp

# Task f(x) = x^3 - x * 4

def f(x):
    return (x**3)-(x*4)

A = sp.Matrix([[-3, 1],
               [2, 1]])

A_cube = A ** 3
A_4 = A * 4
A_result = A_cube - A_4

print("cubed:")
print(A_cube)
print("multiplied:")
print(A_4)
print("Result:")
print(A_result)

test = f(A)
print("def test:")
print(test)
