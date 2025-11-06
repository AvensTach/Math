import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors # Імпортуємо модуль для роботи з кольорами

# Створення загального вікна для графіків
fig = plt.figure(figsize=(14, 14))
fig.suptitle("Візуалізація графіків (Варіант 29)", fontsize=16)

# --- 1) Перша область: Каркасний графік поверхні ---
ax1 = fig.add_subplot(2, 2, 1, projection='3d')

# Параметри для циліндрів
theta = np.linspace(0, 2 * np.pi, 30)
y_range = np.linspace(-5, 5, 10) # Висота першого циліндра
z_range = np.linspace(-5, 5, 10) # Висота другого циліндра

# Циліндр 1: x^2 + z^2 = 9 (радіус 3, вісь Y)
theta_grid, y_grid = np.meshgrid(theta, y_range)
x1 = 3 * np.cos(theta_grid)
z1 = 3 * np.sin(theta_grid)
ax1.plot_wireframe(x1, y_grid, z1, color='blue', alpha=0.6, label='x² + z² = 9')

# Циліндр 2: x^2 + y^2 = 16 (радіус 4, вісь Z)
theta_grid, z_grid = np.meshgrid(theta, z_range)
x2 = 4 * np.cos(theta_grid)
y2 = 4 * np.sin(theta_grid)
ax1.plot_wireframe(x2, y2, z_grid, color='gray', alpha=0.6, label='x² + y² = 16')

ax1.set_title("1. Каркасний графік перетину циліндрів")
ax1.set_xlabel("Вісь X")
ax1.set_ylabel("Вісь Y")
ax1.set_zlabel("Вісь Z")
ax1.legend()

ax1.quiver(0, 0, 0, 10, 0, 0, color='blue', arrow_length_ratio=0.1)
ax1.quiver(0, 0, 0, 0, 10, 0, color='red', arrow_length_ratio=0.1)
ax1.quiver(0, 0, 0, 0, 0, 10, color='green', arrow_length_ratio=0.1)

# --- 2) Друга область: Розсіяний графік поверхні ---
ax2 = fig.add_subplot(2, 2, 2, projection='3d')

# Кількість точок для розсіювання
n_points = 5000

# Циліндр 1: x^2 + z^2 = 9
theta_rand = np.random.uniform(0, 2 * np.pi, n_points)
y_rand = np.random.uniform(-5, 5, n_points)
x1_rand = 3 * np.cos(theta_rand)
z1_rand = 3 * np.sin(theta_rand)
ax2.scatter(x1_rand, y_rand, z1_rand, color='blue', s=1, alpha=0.5)

# Циліндр 2: x^2 + y^2 = 16
theta_rand = np.random.uniform(0, 2 * np.pi, n_points)
z_rand = np.random.uniform(-5, 5, n_points)
x2_rand = 4 * np.cos(theta_rand)
y2_rand = 4 * np.sin(theta_rand)
ax2.scatter(x2_rand, y2_rand, z_rand, color='gray', s=1, alpha=0.5)

ax2.set_title("2. Розсіяний графік перетину циліндрів")
ax2.set_xlabel("Вісь X")
ax2.set_ylabel("Вісь Y")
ax2.set_zlabel("Вісь Z")

ax2.quiver(0, 0, 0, 10, 0, 0, color='blue', arrow_length_ratio=0.1)
ax2.quiver(0, 0, 0, 0, 10, 0, color='red', arrow_length_ratio=0.1)
ax2.quiver(0, 0, 0, 0, 0, 10, color='green', arrow_length_ratio=0.1)

ax3 = fig.add_subplot(2, 2, 3, projection='polar')

phi_bg = np.linspace(0, 2 * np.pi, 200)
r_bg = np.linspace(0, 7, 100)
P, R = np.meshgrid(phi_bg, r_bg)

Z = R - 6 * np.cos(5 * P)


norm = colors.TwoSlopeNorm(vcenter=0)

# ax3.pcolormesh(P, R, Z, cmap='RdBu', shading='auto', norm=norm)


# Дані для самої кривої ("контурний графік")
phi_line = np.linspace(0, 2 * np.pi, 1000)
r_line = 6 * np.cos(5 * phi_line)

ax3.fill(phi_line, r_line, color='blue', alpha=0.7)

# Малювання кривої чорним кольором поверх фону
ax3.plot(phi_line, r_line, color='black', linewidth=2)

ax3.set_title("3. Полярний графік: r = 6cos(5φ)")
ax3.grid(True)

# Автоматичне налаштування відступів між графіками
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Показати результат
plt.show()