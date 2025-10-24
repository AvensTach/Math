import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.path as mpath
import numpy as np
import mpl_toolkits.mplot3d.art3d as art3d

VARIANT = 29
N_POLYGON_SIDES = VARIANT  # Кількість сторін багатокутника: 29
Z_PLANE = 5  # Встановлюємо загальну Z-площину для всіх фігур


def create_polygon_path(sides, center=(0, 0), radius=1):
    """Генерує координати вершин правильного багатокутника."""
    angles = np.linspace(0, 2 * np.pi, sides, endpoint=False)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    return np.column_stack([x, y])


def draw_n_polygon(ax):
    center = (6, 6)
    radius = 4

    verts = create_polygon_path(N_POLYGON_SIDES, center, radius)

    Path = mpath.Path
    codes = [Path.MOVETO] + [Path.LINETO] * (N_POLYGON_SIDES - 2) + [Path.CLOSEPOLY]

    path_patch = mpatches.PathPatch(
        mpath.Path(verts, codes),
        facecolor='#FFE4B5',
        edgecolor='#A52A2A',
        linewidth=2
    )
    ax.add_patch(path_patch)
    art3d.pathpatch_2d_to_3d(path_patch, z=Z_PLANE, zdir="z")

    x_coords = verts[:, 0]
    y_coords = verts[:, 1]
    z_coords = np.full_like(x_coords, Z_PLANE) 

    ax.plot(
        x_coords, y_coords, z_coords,
        marker='>', color='darkred', markersize=8, linestyle='none'
    )

    ax.text(
        center[0], center[1], Z_PLANE,  # Додаємо Z-координату
        f'{N_POLYGON_SIDES}-кутник (Варіант {VARIANT})',
        color='navy',
        fontsize=12,
        weight='bold',
        ha='center',
        va='center'
    )


fig = plt.figure(figsize=(12, 12))

ax = fig.add_subplot(projection='3d')

ax.set_xlim(0, 15)
ax.set_ylim(0, 12)
ax.set_zlim(0, 10) 


draw_n_polygon(ax)

ax.set_title(f'Графічні Примітиви та {N_POLYGON_SIDES}-кутник (Варіант {VARIANT}) на Z={Z_PLANE}', fontsize=16)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_box_aspect((15, 12, 10))  

plt.show()
