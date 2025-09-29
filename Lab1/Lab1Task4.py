import numpy as np
import math

a_length = 1.0
b_length = 4.0
angle_phi = math.pi / 3

# Calculate a * b
a_dot_b = np.around(a_length * b_length * math.cos(angle_phi), decimals=3)
print(f"The dot product a·b is: {a_dot_b}")

# a) (4a + b) . (3a - b) ---
# (4a + b) . (3a - b) = 12(a·a) - 4(a·b) + 3(b·a) - (b·b)
# 12(a·a) - 4(a·b) + 3(b·a) - (b·b) = 12|a|^2 - (a·b) - |b|^2
result_part_a = 12 * (a_length ** 2) - a_dot_b - (b_length ** 2)

print("\n--- a) Solution ---")
print(f"The value of the expression is: {result_part_a}")

# b) |2a + b| ---
# |2a + b|^2 = (2a + b) · (2a + b)
# 4(a·a) + 2(a·b) + 2(b·a) + (b·b)
# 4|a|^2 + 4(a·b) + |b|^2
length_squared = 4 * (a_length ** 2) + 4 * a_dot_b + (b_length ** 2)

# Take the square root to get the magnitude
result_part_b = np.sqrt(length_squared)

print("\n--- b) Solution ---")
print(f"The magnitude squared is: {length_squared}")
print(f"The final magnitude is: {result_part_b}")
