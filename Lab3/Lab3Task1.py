import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import numpy as np
import mpl_toolkits.mplot3d.art3d as art3d  # Import for 3D patch support

# ВАРІАНТ
VARIANT = 29
N_POLYGON_SIDES = VARIANT  # Кількість сторін багатокутника: 29
Z_PLANE = 5  # Встановлюємо загальну Z-площину для всіх фігур



# --- 1. Створення фігур (Примітиви) ---
def draw_primitives(ax):
    # 1. Півколо (Arc)
    semicircle = mpatches.Arc(
        (1, 9), 4, 4,
        angle=0, theta1=0, theta2=180,
        color='blue', linewidth=3
    )
    ax.add_patch(semicircle)
    art3d.pathpatch_2d_to_3d(semicircle, z=Z_PLANE, zdir="z")
    # У 3D plot ax.text вимагає 3 координати (x, y, z)
    ax.text(1, 11.2, Z_PLANE, "Півколо", color='blue', fontsize=10, ha='center')

    # 2. Трикутник (Polygon)
    triangle = mpatches.Polygon(
        [[3, 8], [5, 10], [7, 8]],
        closed=True, color='green', fill=True, alpha=0.8
    )
    ax.add_patch(triangle)
    art3d.pathpatch_2d_to_3d(triangle, z=Z_PLANE, zdir="z")
    ax.text(5, 7.5, Z_PLANE, "Трикутник", color='green', fontsize=10, ha='center')

    # 3. Сектор (Wedge)
    sector = mpatches.Wedge(
        (9, 9), 2, 45, 135,
        color='orange', fill=True, alpha=0.8
    )
    ax.add_patch(sector)
    art3d.pathpatch_2d_to_3d(sector, z=Z_PLANE, zdir="z")
    ax.text(9, 11.2, Z_PLANE, "Сектор", color='orange', fontsize=10, ha='center')

    # 4. Ромб (Custom Path)
    diamond_coords = [[1, 5], [2.5, 6.5], [4, 5], [2.5, 3.5]]
    diamond = mpatches.Polygon(
        diamond_coords,
        closed=True, color='purple', fill=True, alpha=0.7, linewidth=2
    )
    ax.add_patch(diamond)
    art3d.pathpatch_2d_to_3d(diamond, z=Z_PLANE, zdir="z")
    ax.text(2.5, 2.8, Z_PLANE, "Ромб", color='purple', fontsize=10, ha='center')

    # 5. Прямокутник (Rectangle)
    rectangle = mpatches.Rectangle(
        (5, 4), 3, 2,
        color='brown', fill=False, linewidth=3, linestyle='--'
    )
    ax.add_patch(rectangle)
    art3d.pathpatch_2d_to_3d(rectangle, z=Z_PLANE, zdir="z")
    ax.text(6.5, 3.5, Z_PLANE, "Прямокутник", color='brown', fontsize=10, ha='center')

    # 6. Стрілка (Arrow)
    arrow = mpatches.Arrow(
        9, 5, -2, 0,
        width=0.4, color='red'
    )
    ax.add_patch(arrow)
    art3d.pathpatch_2d_to_3d(arrow, z=Z_PLANE, zdir="z")
    ax.text(8, 4.3, Z_PLANE, "Стрілка", color='red', fontsize=10, ha='left')


# --- Налаштування графічної області ---
fig = plt.figure(figsize=(12, 12))

# *** КРИТИЧНА ЗМІНА: Створюємо 3D осі ***
ax = fig.add_subplot(projection='3d')

# Встановлення меж графіка
ax.set_xlim(0, 15)
ax.set_ylim(0, 12)
ax.set_zlim(0, 10)  # Додаємо межі для осі Z
# set_aspect('equal') для 3D не використовується, натомість використовується ax.set_box_aspect

# Малювання фігур
draw_primitives(ax)

# Налаштування 3D-вигляду та міток
ax.set_title(f'Графічні Примітиви (Варіант {VARIANT}) на Z={Z_PLANE}', fontsize=16)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_box_aspect((15, 12, 10))  # Налаштування співвідношення сторін 3D-вікна

plt.show()