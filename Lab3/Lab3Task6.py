import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

plt.switch_backend('TkAgg')

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)

Z1 = X ** 3 - 3 * X * Y ** 2 + 18 * Y

Z2 = 3 * (X ** 2) * Y - Y ** 3 - 6 * X

Z_max = np.maximum(Z1, Z2)

norm1 = plt.Normalize(Z1.min(), Z1.max())
norm2 = plt.Normalize(Z2.min(), Z2.max())

cmap1 = plt.cm.plasma
cmap2 = plt.cm.viridis

mask_z1_higher = Z1 > Z2

colors = np.where(mask_z1_higher[..., np.newaxis], cmap1(norm1(Z1)), cmap2(norm2(Z2)))

ax.plot_surface(X, Y, Z_max, facecolors=colors, edgecolor='none')

ax.set_xlabel('X axis', fontsize=12)
ax.set_ylabel('Y axis', fontsize=12)
ax.set_zlabel('Z axis', fontsize=12)
ax.set_title('Plot of the Higher Surface at Each Point', fontsize=16)

plasma_patch = mpatches.Patch(color=plt.cm.plasma(0.5), label="'z = x³ - 3xy² + 18y' is higher")
viridis_patch = mpatches.Patch(color=plt.cm.viridis(0.5), label="'z = 3x²y - y³ - 6x' is higher")

ax.legend(handles=[plasma_patch, viridis_patch])

ax.view_init(elev=20, azim=-65)

ax.grid(True)
plt.show()
