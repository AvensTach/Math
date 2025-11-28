import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Налаштування стилю графіків
plt.style.use('seaborn-v0_8-whitegrid')

# 1. Визначення функції
def f1(x):
    return x * np.sqrt(9 - x**2)

# 2. Чисельне інтегрування
result1, error1 = integrate.quad(f1, 0, 3)
print(f"Завдання 8.1.29: Площа S ≈ {result1:.6f} (похибка {error1:.2e})")

# 3. Побудова графіка
x = np.linspace(0, 3, 200)
y = f1(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'b-', label=r'$y = x\sqrt{9-x^2}$', linewidth=2)
plt.plot(x, np.zeros_like(x), 'k-', label=r'$y=0$', linewidth=1)
plt.fill_between(x, y, 0, color='skyblue', alpha=0.4, label='Шукана площа')

plt.title('Графік до завдання 8.1.29')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.xlim(0, 3.1)
plt.ylim(0, np.max(y)*1.1)
plt.show()

# 1. Визначення підінтегральної функції для однієї пелюстки
def polar_integrand(phi):
    rho_outer = 4 * np.sin(2 * phi)
    rho_inner = 2 * np.sqrt(3)
    return 0.5 * (rho_outer**2 - rho_inner**2)

# 2. Чисельне інтегрування (одна частина)
phi_start = np.pi / 6
phi_end = np.pi / 3
area_part, error2 = integrate.quad(polar_integrand, phi_start, phi_end)
total_area2 = 4 * area_part
print(f"Завдання 8.2.29: Повна площа S ≈ {total_area2:.6f}")

# 3. Побудова графіка в полярних координатах
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')

# Повний діапазон кутів для малювання
phi = np.linspace(0, 2*np.pi, 1000)
rho_curve = 4 * np.sin(2 * phi)
rho_circle = np.full_like(phi, 2 * np.sqrt(3))

ax.plot(phi, rho_curve, 'r-', label=r'$\rho = 4 \sin 2\varphi$')
ax.plot(phi, rho_circle, 'b--', label=r'$\rho = 2\sqrt{3}$')

# Заливка області (для всіх 4 частин)
for k in range(4):
    phi_fill = np.linspace(phi_start + k*np.pi/2, phi_end + k*np.pi/2, 100)
    rho_outer_fill = 4 * np.sin(2 * phi_fill)
    rho_inner_fill = np.full_like(phi_fill, 2 * np.sqrt(3))
    # Використовуємо fill_between для полярних координат
    ax.fill_between(phi_fill, rho_inner_fill, rho_outer_fill, color='orange', alpha=0.5)

ax.set_title('Графік до завдання 8.2.29 (Полярні координати)', va='bottom')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.show()

# 1. Визначення функцій x від y
def get_t_from_y(y):
    # t для лівої частини арки (0 < t < pi)
    return np.arccos(1 - y / 8)

def x_left(y):
    t = get_t_from_y(y)
    return 8 * (t - np.sin(t))

def x_right(y):
    t_left = get_t_from_y(y)
    t_right = 2 * np.pi - t_left # Симетрія відносно t=pi
    return 8 * (t_right - np.sin(t_right))

def integrand_y(y):
    return x_right(y) - x_left(y)

# 2. Чисельне інтегрування по y
result3, error3 = integrate.quad(integrand_y, 4, 12)
print(f"Завдання 8.3.29: Площа S ≈ {result3:.6f}")

# 3. Побудова графіка
t_plot = np.linspace(0, 2*np.pi, 300)
x_cycloid = 8 * (t_plot - np.sin(t_plot))
y_cycloid = 8 * (1 - np.cos(t_plot))

plt.figure(figsize=(10, 6))
plt.plot(x_cycloid, y_cycloid, 'g-', label='Циклоїда', linewidth=2)
plt.axhline(y=4, color='r', linestyle='--', label='y=4')
plt.axhline(y=12, color='m', linestyle='--', label='y=12')

# Створення полігону для заливки складної області
y_fill = np.linspace(4, 12, 100)
x_l_fill = x_left(y_fill)
x_r_fill = x_right(y_fill)
# Об'єднуємо точки для замкнутого контуру: вверх по правій стороні, вниз по лівій
x_poly = np.concatenate([x_r_fill, x_l_fill[::-1]])
y_poly = np.concatenate([y_fill, y_fill[::-1]])
plt.fill(x_poly, y_poly, color='lime', alpha=0.3, label='Шукана площа')

plt.title('Графік до завдання 8.3.29')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# 1. Визначення функції
def f4(x):
    # Додаємо невелику перевірку, щоб уникнути помилок обчислення sqrt біля меж
    mask = (x >= 0) & (x <= 0.5)
    res = np.zeros_like(x)
    res[mask] = 4 * np.arccos(x[mask]) - np.sqrt(x[mask] - x[mask]**2)
    return res

# Функція для інтегратора (приймає скаляр)
def f4_scalar(x):
     return 4 * np.arccos(x) - np.sqrt(x - x**2)

# 2. Чисельне інтегрування
result4, error4 = integrate.quad(f4_scalar, 0, 0.5)
print(f"Завдання 8.4.29: Площа S ≈ {result4:.6f}")

# 3. Побудова графіка
x = np.linspace(0, 0.5, 200)
y = f4(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'purple', label=r'$y = 4 \arccos x - \sqrt{x - x^2}$', linewidth=2)
plt.fill_between(x, y, 0, color='violet', alpha=0.4, label='Шукана площа')

plt.title('Графік до завдання 8.4.29')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.xlim(-0.05, 0.55)
plt.ylim(0, np.max(y)*1.1)
plt.show()

# 1. Визначення параметричних функцій та підінтегрального виразу
def x_t(t):
    return 2 * t - np.sin(2 * t)

def y_t(t):
    return 2 * np.cos(t)**2

def parametric_integrand(t):
    # y(t) * x'(t)
    # x'(t) = 2 - 2*cos(2t)
    # y(t) = 2*cos^2(t)
    return (2 * np.cos(t)**2) * (2 - 2 * np.cos(2 * t))

# 2. Чисельне інтегрування
result5, error5 = integrate.quad(parametric_integrand, 0, 2 * np.pi)
print(f"Завдання 8.5.29: Площа S ≈ {result5:.6f}")
# Аналітичний результат для перевірки: 2*pi ≈ 6.283185

# 3. Побудова графіка
t = np.linspace(0, 2 * np.pi, 400)
x_val = x_t(t)
y_val = y_t(t)

plt.figure(figsize=(10, 5))
plt.plot(x_val, y_val, 'darkorange', label=r'Параметрична крива', linewidth=2)
plt.fill_between(x_val, y_val, 0, color='wheat', alpha=0.5, label='Шукана площа')

plt.title('Графік до завдання 8.5.29')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
# Встановимо рівний масштаб осей для коректного відображення форми
plt.axis('equal')
plt.ylim(0, 2.5)
plt.show()