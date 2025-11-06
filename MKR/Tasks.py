# variant = 5
import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend('TkAgg')

print("Завдання 1:")

A = np.array([3, -2, 2])
B = np.array([-3, 1, 0])
C = np.array([-6, 3, 1])
D = np.array([6, -3, 5])

vec_AB = B - A
vec_BC = C - B
vec_CD = D - C
vec_DA = A - D

print(f"Вектор AB = {vec_AB}")
print(f"Вектор CD = {vec_CD}")
print(f"Вектор BC = {vec_BC}")
print(f"Вектор DA = {vec_DA}")


cross_AB_CD = np.cross(vec_AB, vec_CD)
cross_BC_DA = np.cross(vec_BC, vec_DA)

is_AB_CD_parallel = cross_AB_CD.all(0)
is_BC_DA_parallel = cross_BC_DA.all(0)



print(f"\nAB || CD? {is_AB_CD_parallel}")
print(f"BC || DA? {is_BC_DA_parallel}")

if is_AB_CD_parallel != is_BC_DA_parallel:
    print("Висновок: Фігура є трапецією.")
else:
    print("Висновок: Фігура не є трапецією (або є паралелограмом).")

# Знаходження косинусів внутрішніх кутів при більшій основі
len_AB = np.linalg.norm(vec_AB)
len_CD = np.linalg.norm(vec_CD)

print(f"\nДовжина основи AB = {len_AB:.1f}")
print(f"Довжина основи CD = {len_CD:.1f}")

if len_CD > len_AB:
    print("Більша основа - CD. Шукаємо кути C і D.")
    # Кут C (між векторами CB і CD)
    vec_CB = -vec_BC
    vec_DC = -vec_CD

    len_CB = np.linalg.norm(vec_CB)
    len_DA = np.linalg.norm(vec_DA)

    # cos(C) = (CB · CD) / (|CB| * |CD|)
    dot_C = np.dot(vec_CB, vec_CD)
    cos_C = dot_C / (len_CB * len_CD)

    # cos(D) = (DC · DA) / (|DC| * |DA|)
    dot_D = np.dot(vec_DC, vec_DA)
    cos_D = dot_D / (len_DA * len_CD)  # |DC| = |CD|

    print(f"cos(C) = {cos_C:.4f} (Точне значення: 44 / (14 * sqrt(14)) = 22 / (7*sqrt(14)))")
    print(f"cos(D) = {cos_D:.4f} (Точне значення: 54 / (14 * sqrt(19)) = 27 / (7*sqrt(19)))")
else:
    print("Більша основа - AB. Шукаємо кути A і B.")
    # Кут A (між векторами AD і AB)
    vec_AD = -vec_DA
    # Кут B (між векторами BA і BC)
    vec_BA = -vec_AB

    # Знаходимо довжини сторін, що утворюють кути
    len_AD = np.linalg.norm(vec_AD)  # Це те ж саме, що np.linalg.norm(vec_DA)
    len_BC = np.linalg.norm(vec_BC)

    # cos(A) = (AD · AB) / (|AD| * |AB|)
    dot_A = np.dot(vec_AD, vec_AB)
    cos_A = dot_A / (len_AD * len_AB)

    # cos(B) = (BA · BC) / (|BA| * |BC|)
    dot_B = np.dot(vec_BA, vec_BC)
    cos_B = dot_B / (len_AB * len_BC)  # Оскільки |BA| = |AB|

    print(f"cos(A) = {cos_A:.4f}")
    print(f"cos(B) = {cos_B:.4f}")


fig = plt.figure(figsize=(14, 7))
ax1 = fig.add_subplot(121, projection='3d')

points = np.array([A, B, C, D, A])

# Малюємо лінії
ax1.plot(points[:, 0], points[:, 1], points[:, 2], 'bo-')

# Додаємо мітки
ax1.text(A[0], A[1], A[2], 'A (3,-2,2)', color='red')
ax1.text(B[0], B[1], B[2], 'B (-3,1,0)', color='red')
ax1.text(C[0], C[1], C[2], 'C (-6,3,1)', color='red')
ax1.text(D[0], D[1], D[2], 'D (6,-3,5)', color='red')

ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Завдання 1: Трапеція ABCD')
ax1.grid(True)

# --- Завдання 2: Куб і параболи ---

print("\n--- Завдання 2: Куб і параболи ---")
print("Малюємо куб та параболи на його гранях...")

ax2 = fig.add_subplot(122, projection='3d')

# 2. Малюємо 12 ребер, згрупувавши їх за осями
xyz_values = [0, 1]

# 4 ребра, паралельні осі X (змінюється 'x', 'y' та 'z' фіксовані)
for y in xyz_values:
    for z in xyz_values:
        ax2.plot3D([0, 1], [y, y], [z, z], color="k")

# 4 ребра, паралельні осі Y (змінюється 'y', 'x' та 'z' фіксовані)
for x in xyz_values:
    for z in xyz_values:
        ax2.plot3D([x, x], [0, 1], [z, z], color="k")

# 4 ребра, паралельні осі Z (змінюється 'z', 'x' та 'y' фіксовані)
for x in xyz_values:
    for y in xyz_values:
        ax2.plot3D([x, x], [y, y], [0, 1], color="k")

# 3. Малюємо параболи на гранях
t = np.linspace(0, 1, 20)

# Парабола на верхній грані (z=1)
# y = 4*(x-0.5)^2
x_p1 = t
y_p1 = 4 * (t - 0.5) ** 2
z_p1 = np.ones_like(t)
ax2.plot(x_p1, y_p1, z_p1, 'r-', linewidth=2, label='Парабола на z=1')

# Парабола на передній грані (y=1)
# z = -4*(x-0.5)^2 + 1
x_p2 = t
y_p2 = np.ones_like(t)
z_p2 = -4 * (t - 0.5) ** 2 + 1
ax2.plot(x_p2, y_p2, z_p2, 'g-', linewidth=2, label='Парабола на y=1')

# Парабола на бічній грані (x=1)
# z = 4*(y-0.5)^2
x_p3 = np.ones_like(t)
y_p3 = t
z_p3 = 4 * (t - 0.5) ** 2
ax2.plot(x_p3, y_p3, z_p3, 'b-', linewidth=2, label='Парабола на x=1')

# --- 3 "невидимі" грані (пунктирні лінії) ---

# Парабола на нижній грані (z=0)
x_p4 = t
y_p4 = 4 * (t - 0.5) ** 2
z_p4 = np.zeros_like(t) # z=0
ax2.plot(x_p4, y_p4, z_p4, 'r--', linewidth=2, label='Парабола на z=0')

# Парабола на задній грані (y=0)
x_p5 = t
y_p5 = np.zeros_like(t) # y=0
z_p5 = -4 * (t - 0.5) ** 2 + 1
ax2.plot(x_p5, y_p5, z_p5, 'g--', linewidth=2, label='Парабола на y=0')

# Парабола на бічній грані (x=0)
x_p6 = np.zeros_like(t) # x=0
y_p6 = t
z_p6 = 4 * (t - 0.5) ** 2
ax2.plot(x_p6, y_p6, z_p6, 'b--', linewidth=2, label='Парабола на x=0')


ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Завдання 2: Куб з параболами')
ax2.legend(fontsize='medium') # Трохи зменшимо шрифт легенди, бо багато елементів
ax2.grid(True)

# Показати обидва графіки
plt.tight_layout()
plt.show()
