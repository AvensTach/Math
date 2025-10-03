import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

Z = np.arcsin((X / Y)) + Y * X - Y

plt.contour(X, Y, Z, levels=0, colors='b')
plt.text(-1, -3.75, r'$arcsin(x/y) + xy = y', fontsize=10, color='red', rotation=90, ha='center')

plt.axhline(0, color='b', linewidth=0.5)
plt.axvline(0, color='b', linewidth=0.5)
plt.grid(True)

plt.gca().set_aspect('equal', adjustable='box')
plt.show()

t = np.linspace(0, 1, 1000)
y = np.arcsin(np.sqrt(1 - t))
x = np.arccos(np.sqrt(1 - t ** 2))

plt.figure(figsize=(10, 10))
plt.plot(x, y, color='b', label='крива: $y = arcsin(sqrt(1-t))$, $y = arcsin(sqrt(1-t^2)$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Параметрично задана крива')
plt.legend()
plt.grid(True)

plt.show()

a = 1
b = 0.5

phi = np.linspace(0, 2 * np.pi, 1000)

r = a / (1 + b * np.sin(phi))

x = r * np.cos(phi)
y = r * np.sin(phi)

plt.figure(figsize=(10, 10))
plt.polar(phi, r, color='green', label="r = 1/(1+0.5*sin(phi))")
plt.title('Крива другого порядку в полярній системі координат')
plt.legend()
plt.grid(True)
plt.show()

x = np.linspace(-10, 10, 400)
y = np.linspace(-20, 20, 400)
X, Y = np.meshgrid(x, y)

# 2. Визначення функції Z = 23x^2 - 72xy + 2y^2 + 25
Z = 23 * X ** 2 - 72 * X * Y + 2 * Y ** 2 + 25

plt.figure(figsize=(10, 10))

plt.contour(X, Y, Z, levels=[0], colors='blue', linewidths=6)

plt.contour(X, Y, Z, levels=[0], colors='green', linewidths=4)

plt.contour(X, Y, Z, levels=[0], colors='red', linewidths=2)

text_label = r'Вказати рівняння кривої: $23x^2 - 72xy + 2y^2 + 25 = 0$'
alpha = 154
text_color = 'purple'

plt.text(0, -5, text_label, fontsize=12, color=text_color, rotation=alpha, ha='center')

axis_color = 'black'

plt.axhline(0, color=axis_color, linewidth=0.5)
plt.axvline(0, color=axis_color, linewidth=0.5)

plt.grid(True, linestyle=':', alpha=0.7, color=axis_color)
plt.title('Побудова кольорової гіперболи ($23x^2 - 72xy + 2y^2 + 25 = 0$)')
plt.xlabel('X')
plt.ylabel('Y')
plt.gca().set_aspect('equal', adjustable='box')

plt.show()


def f(x):
    """Функція f(x) = x^2 - 2"""
    return x ** 2 - 2


def g(x):
    """Функція g(x) = cos(x + 3)"""
    return np.cos(x + 3)


x = np.linspace(-5, 5, 1000)
y_f = f(x)
y_g = g(x)

diff = y_f - y_g

zero_crossings_indices = np.where(np.diff(np.sign(diff)))[0]

intersection_points_x = x[zero_crossings_indices]

intersection_points_y = f(intersection_points_x)

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 10), sharex=True)

# Назва вікна
fig.suptitle('Графіки функцій $f(x)$ та $g(x)$ з точками перетину', fontsize=16, color='darkred')

# --- ПЕРШИЙ ПІДГРАФІК: f(x) та g(x) разом ---
ax1 = axes[0]
ax1.plot(x, y_f, color='purple', linewidth=2, linestyle='-', label=r'$f(x) = x^2 - 2$')

ax1.plot(intersection_points_x, intersection_points_y, 'o', color='red', markersize=8, label='Точки перетину')
for x_val, y_val in zip(intersection_points_x, intersection_points_y):
    ax1.annotate(f'({x_val:.3f}, {y_val:.3f})',
                 (x_val, y_val),
                 textcoords="offset points",
                 xytext=(5, 10),
                 ha='center',
                 color='red',
                 fontsize=9)

ax1.set_title('Графіки $f(x)$ та $g(x)$ разом', fontsize=14)
ax1.axhline(0, color='black', linewidth=1, linestyle='--')
ax1.axvline(0, color='black', linewidth=1, linestyle='--')
ax1.set_ylabel("Вісь Y (Спільний графік)", fontsize=12, color='darkblue')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper right')

ax2 = axes[1]

ax2.plot(x, y_g, color='yellowgreen', linewidth=4, linestyle='-', label=r'$g(x) = \cos(x + 3)$')

ax2.plot(intersection_points_x, intersection_points_y, 'o', color='red', markersize=8, label='Точки перетину')
for x_val, y_val in zip(intersection_points_x, intersection_points_y):
    ax2.annotate(f'({x_val:.3f}, {y_val:.3f})',
                 (x_val, y_val),
                 textcoords="offset points",
                 xytext=(5, -15),  # Змінюємо зміщення Y, щоб не накластися на інші підписи
                 ha='center',
                 color='red',
                 fontsize=9)

ax2.set_title('Графіки $f(x)$ та $g(x)$ (друга візуалізація)', fontsize=14)
ax2.axhline(0, color='black', linewidth=1, linestyle='--')  # Вісь X
ax2.axvline(0, color='black', linewidth=1, linestyle='--')  # Вісь Y
ax2.set_xlabel("Вісь X", fontsize=14, color='darkblue')
ax2.set_ylabel("Вісь Y (Друга візуалізація)", fontsize=12, color='darkblue')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='lower left')

# Налаштування відступу між підграфіками
plt.tight_layout(rect=[0, 0, 1, 1])
plt.show()
