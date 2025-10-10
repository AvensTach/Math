import numpy as np

A = np.array([-5, 0, 3])
B = np.array([2, 1, 5])
C = np.array([-4, 2, -1])
D = np.array([0, 0, 3])


vector_AB = B - A
vector_AC = C - A

cross_product_vec = np.cross(vector_AB, vector_AC)

area_ABC = 0.5 * np.linalg.norm(cross_product_vec)


vector_AD = D - A

scalar_triple_product = np.dot(vector_AD, cross_product_vec)

volume_ABCD = (1/6) * np.abs(scalar_triple_product)

# Print the results
print("--- Results ---")
print(f"The Area of face ABC is: {area_ABC:.4f} square units")
print(f"The Volume of tetrahedron ABCD is: {volume_ABCD:.4f} cubic units")