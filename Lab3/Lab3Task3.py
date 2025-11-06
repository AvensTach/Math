import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.switch_backend('TkAgg')


# Helper function to generate cylinder data
def get_cylinder_data(R, axis_index, V_range=5):
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(-V_range, V_range, 50)
    U, V = np.meshgrid(u, v)

    coords = [R * np.cos(U), R * np.sin(U), V]

    if axis_index == 1:  # Cylinder x^2 + z^2 = R^2 (Axis Y)
        return coords[0], coords[2], coords[1]  # X, Y, Z = R*cos, V, R*sin
    else:  # Cylinder x^2 + y^2 = R^2 (Axis Z)
        return coords[0], coords[1], coords[2]  # X, Y, Z = R*cos, R*sin, V


# --- Parameters ---
R1 = 3  # Radius for Cylinder 1: x^2 + z^2 = 9 (Axis Y)
R2 = 4  # Radius for Cylinder 2: x^2 + y^2 = 16 (Axis Z)
V_RANGE = 5  # Height/Length of the cylinders

# --- Plotting ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Cylinder 1: x^2 + z^2 = 9 (Axis Y is the axis of rotation)
X1, Y1, Z1 = get_cylinder_data(R=R1, axis_index=1, V_range=V_RANGE)
# Changed color to light blue and alpha for consistency with example image
ax.plot_surface(X1, Y1, Z1, color='cornflowerblue', alpha=0.8, rstride=2, cstride=2)

# 2. Cylinder 2: x^2 + y^2 = 16 (Axis Z is the axis of rotation)
X2, Y2, Z2 = get_cylinder_data(R=R2, axis_index=2, V_range=V_RANGE)
# Changed color to grey and alpha for consistency
ax.plot_surface(X2, Y2, Z2, color='darkgrey', alpha=0.8, rstride=2, cstride=2)

# --- Axis Labels and Title ---
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set equal aspect ratio for better visualization
ax.set_box_aspect([1, 1, 1])

# Set limits to include the cylinders completely
max_coord = max(R1, R2, V_RANGE) + 1  # Add some padding
ax.set_xlim(-max_coord, max_coord)
ax.set_ylim(-max_coord, max_coord)
ax.set_zlim(-max_coord, max_coord)

ax.quiver(0, 0, 0, 10, 0, 0, color='blue', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 10, 0, color='red', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0, 10, color='green', arrow_length_ratio=0.1)

# Add grid lines and turn off axis panes for a cleaner look
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(True, linestyle=':', alpha=0.7)

ax.view_init(elev=20, azim=45)  # Experiment with these values!

plt.suptitle('Перетин двох кругових циліндрів', fontsize=16)  # Main title
plt.title(r'$x^2 + z^2 = 9$, $x^2 + y^2 = 16$', fontsize=14, loc='center', pad=-10)  # Subtitle for equations

plt.show()
