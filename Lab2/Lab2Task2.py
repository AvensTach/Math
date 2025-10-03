import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import numpy as np

# ВАРІАНТ
VARIANT = 29
N_POLYGON_SIDES = VARIANT  # Кількість сторін багатокутника: 29


# --- Функція для малювання N-кутника ---
def create_polygon_path(sides, center=(0, 0), radius=1):
    """Генерує координати вершин правильного багатокутника."""
    angles = np.linspace(0, 2 * np.pi, sides, endpoint=False)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return np.column_stack([x, y])


# --- 1. Створення фігур (Примітиви) ---
def draw_primitives(ax):
    # 1. Півколо (Arc)
    semicircle = mpatches.Arc(
        (1, 9), 4, 4,  # (x, y), width, height
        angle=0, theta1=0, theta2=180,  # Кути: від 0 до 180 градусів
        color='blue', linewidth=3
    )
    ax.add_patch(semicircle)
    ax.text(1, 11.2, "Півколо", color='blue', fontsize=10, ha='center')

    # 2. Трикутник (Polygon)
    triangle = mpatches.Polygon(
        [[3, 8], [5, 10], [7, 8]],
        closed=True, color='green', fill=True, alpha=0.8
    )
    ax.add_patch(triangle)
    ax.text(5, 7.5, "Трикутник", color='green', fontsize=10, ha='center')

    # 3. Сектор (Wedge)
    sector = mpatches.Wedge(
        (9, 9), 2, 45, 135,  # (x, y), radius, theta1, theta2
        color='orange', fill=True, alpha=0.8
    )
    ax.add_patch(sector)
    ax.text(9, 11.2, "Сектор", color='orange', fontsize=10, ha='center')

    # 4. Ромб (Custom Path)
    diamond_coords = [[1, 5], [2.5, 6.5], [4, 5], [2.5, 3.5]]
    diamond = mpatches.Polygon(
        diamond_coords,
        closed=True, color='purple', fill=True, alpha=0.7, linewidth=2
    )
    ax.add_patch(diamond)
    ax.text(2.5, 2.8, "Ромб", color='purple', fontsize=10, ha='center')

    # 5. Прямокутник (Rectangle)
    rectangle = mpatches.Rectangle(
        (5, 4), 3, 2,  # (x, y) кута, width, height
        color='brown', fill=False, linewidth=3, linestyle='--'
    )
    ax.add_patch(rectangle)
    ax.text(6.5, 3.5, "Прямокутник", color='brown', fontsize=10, ha='center')

    # 6. Стрілка (Arrow)
    arrow = mpatches.Arrow(
        9, 5, -2, 0,
        width=0.4, color='red'
    )
    ax.add_patch(arrow)
    ax.text(8, 4.3, "Стрілка", color='red', fontsize=10, ha='left')


# --- 2. Створення N-багатокутника (29-кутник) ---
def draw_n_polygon(ax):
    center = (13, 6)
    radius = 3.5

    # 1. Створення контуру багатокутника (29-кутник)
    verts = create_polygon_path(N_POLYGON_SIDES, center, radius)

    # 2. Створення Path з контуром-стрілочками
    Path = mpath.Path

    codes = [Path.MOVETO] + [Path.LINETO] * (N_POLYGON_SIDES - 2) + [Path.CLOSEPOLY]

    # Створення PathPatch для заповнення
    path_patch = mpatches.PathPatch(
        mpath.Path(verts, codes),
        facecolor='#FFE4B5',  # Кольорова заливка (світло-помаранчевий)
        edgecolor='#A52A2A',  # Колір контуру (коричневий)
        linewidth=2
    )
    ax.add_patch(path_patch)

    # Додавання стрілочок по кутах (маркери)
    for x, y in verts:
        ax.plot(x, y, marker='>', color='darkred', markersize=8, linestyle='none')

    # 3. Додавання тексту в середині
    ax.text(
        center[0], center[1],
        f'{N_POLYGON_SIDES}-кутник (Варіант {VARIANT})',
        color='navy',
        fontsize=12,
        weight='bold',
        ha='center',
        va='center'
    )


# --- Налаштування графічної області ---
fig, ax = plt.subplots(figsize=(12, 12))

# Встановлення меж графіка для вміщення всіх фігур
ax.set_xlim(0, 15)
ax.set_ylim(0, 12)
ax.set_aspect('equal', adjustable='box')  # Зберігаємо пропорції
ax.set_title(f'Графічні Примітиви та {N_POLYGON_SIDES}-кутник (Варіант {VARIANT})', fontsize=16)
ax.set_xticks(np.arange(0, 16, 1))
ax.set_yticks(np.arange(0, 13, 1))
ax.grid(True, linestyle=':', alpha=0.6)

# Малювання фігур
draw_primitives(ax)
# Малювання багатокутника в центральній області (координати 5, 5)
draw_n_polygon(ax)

plt.tight_layout()
plt.show()