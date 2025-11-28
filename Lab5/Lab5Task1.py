import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

plt.switch_backend('TkAgg')

VARIANT = 29
sp.init_printing(use_unicode=True)
# репата ст. 203 № 2.4.29

x = sp.symbols('x')

y1 = (sp.cos(x + (5 * sp.pi / 2)) * sp.tan(x)) / sp.asin(2 * x)

y2 = (2 ** x - 1) / sp.ln(1 + 2 * x)

limit_y1 = sp.limit(y1, x, 0)
limit_y2 = sp.limit(y2, x, 0)
sp.pprint("Репета-1 завдання 2.4.29:")
sp.pprint(f'Ліміт 1 = {limit_y1}, ліміт 2 = {limit_y2}')

# Репета-1 ст. 248 № 4.4.29
print("-" * 30)
y = (5 * x + 2) ** sp.sin(x)

dy_dx = sp.diff(y, x)

print("Функція y:")
sp.pprint(y)

print("\nПохідна dy/dx:")
sp.pprint(dy_dx)
print("-" * 30)

# Репета-2 ст. 109 № 2.1.29

P3 = -x ** 3 - x ** 2 + 11 * x + 3

full_factors = sp.factor(P3, extension=[sp.sqrt(3)])

print("Оригінальний многочлен:")
sp.pprint(P3)

print("\nРезультат розкладання (над раціональними числами):")
sp.pprint(full_factors)
print("-" * 30)

# Репета-2 ст. 166 № 29

func = 1 / (sp.sqrt(4 + sp.exp(x)))

result = sp.integrate(func, (x, sp.ln(5), sp.ln(12)))

print('Підінтегральний вираз')
sp.pprint(func)

print("Результат обчислення")
sp.pprint(result)

print("\nСпрощений вигляд")
sp.pprint(sp.simplify(result))

print("\nЧислове значення (приблизно)")
print(result.evalf())

print("-" * 30)

# Репета-2 ст. 28-60 № 3.1.29
x, y = sp.symbols('x y')

expression_inside = x**2 + 3*x*y - 4*x + 3*y - 1
z_func = expression_inside**(sp.Rational(1, 3))

# координати М
x0_val = 1
y0_val = 2

z0_val = z_func.subs({x: x0_val, y: y0_val})

dz_dx = sp.diff(z_func, x)
dz_dy = sp.diff(z_func, y)

slope_x = dz_dx.subs({x: x0_val, y: y0_val})
slope_y = dz_dy.subs({x: x0_val, y: y0_val})

tangent_plane_eq = z0_val + slope_x * (x - x0_val) + slope_y * (y - y0_val)

print("--- Результати розрахунків ---")
print(f"Точка дотику P({x0_val}, {y0_val}, {z0_val})")
print(f"Похідна по x в точці M: {slope_x}")
print(f"Похідна по y в точці M: {slope_y}")
print("\nРівняння дотичної площини (z = ...):")
sp.pprint(tangent_plane_eq)

print("\nРівняння нормалі (канонічне):")
print(f"(x - {x0_val}) / {slope_x} = (y - {y0_val}) / {slope_y} = (z - {z0_val}) / -1")

# Візуалізація (Matplotlib)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

range_plot = 2
x_vals = np.linspace(x0_val - range_plot, x0_val + range_plot, 50)
y_vals = np.linspace(y0_val - range_plot, y0_val + range_plot, 50)
X, Y = np.meshgrid(x_vals, y_vals)

Z_surface = np.cbrt(X**2 + 3*X*Y - 4*X + 3*Y - 1)

plane_lambda = sp.lambdify((x, y), tangent_plane_eq, 'numpy')
Z_plane = plane_lambda(X, Y)

ax.plot_surface(X, Y, Z_surface, alpha=0.5, color='cyan', label='Поверхня z')
ax.plot_surface(X, Y, Z_plane, alpha=0.3, color='orange', label='Дотична площина')

t = np.linspace(-2, 2, 10)
norm_x = x0_val + float(slope_x) * t
norm_y = y0_val + float(slope_y) * t
norm_z = float(z0_val) - 1 * t

ax.plot(norm_x, norm_y, norm_z, color='yellow', linewidth=3, label='Нормаль')
ax.scatter(x0_val, y0_val, float(z0_val), color='black', s=100, label='Точка M')

length = range_plot * 1.5
origin_x, origin_y, origin_z = x0_val, y0_val, float(z0_val)

ax.quiver(origin_x, origin_y, origin_z, length, 0, 0, color='r', arrow_length_ratio=0.1, linewidth=1.5)
ax.text(origin_x+length, origin_y, origin_z, "X", color='r', fontsize=12, fontweight='bold')

ax.quiver(origin_x, origin_y, origin_z, 0, length, 0, color='g', arrow_length_ratio=0.1, linewidth=1.5)
ax.text(origin_x, origin_y+length, origin_z, "Y", color='g', fontsize=12, fontweight='bold')

ax.quiver(origin_x, origin_y, origin_z, 0, 0, length, color='b', arrow_length_ratio=0.1, linewidth=1.5)
ax.text(origin_x, origin_y, origin_z+length, "Z", color='b', fontsize=12, fontweight='bold')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Дотична та нормаль у точці M({x0_val}, {y0_val})')

cyan_patch = mlines.Line2D([], [], color='cyan', alpha=0.5, label='Поверхня')
orange_patch = mlines.Line2D([], [], color='orange', alpha=0.5, label='Дотична площина')
red_line = mlines.Line2D([], [], color='yellow', label='Нормаль')
plt.legend(handles=[cyan_patch, orange_patch, red_line])

plt.show()

print("-" * 30)

# Репета-2 ст. 58-60 № 3.2.29

x, y, z = sp.symbols('x y z')
u = sp.sqrt(x**2 + y**2 + z**2)

# Координати точки M
vals = {x: 1, y: 2, z: -2}

grad_u = sp.Matrix([sp.diff(u, var) for var in (x, y, z)])

grad_at_M = grad_u.subs(vals)

vec_l = sp.Matrix([1, 2, -2])

len_l = vec_l.norm()
unit_vec_l = vec_l / len_l

derivative_direction = grad_at_M.dot(unit_vec_l)

print("--- Проміжні значення ---")
print(f"Градієнт у точці M: {grad_at_M}")
print(f"Вектор напрямку: {vec_l}")
print(f"Одиничний вектор напрямку: {unit_vec_l}")

print("\n--- Відповідь (Похідна за напрямком) ---")
sp.pprint(derivative_direction)

print("-" * 30)



# Репета-2 ст. 58-60 № 3.3.29

sp.init_printing(use_unicode=True)
x, y = sp.symbols('x y', real=True)

z = x * sp.sqrt(y) - x ** 2 - y + 6 * x

dz_dx = sp.diff(z, x)
dz_dy = sp.diff(z, y)

print("--- Перші похідні ---")
print(f"dz/dx = {dz_dx}")
print(f"dz/dy = {dz_dy}")

critical_points = sp.solve([dz_dx, dz_dy], (x, y))
print(f"\nСтаціонарні точки: {critical_points}")

A = sp.diff(z, x, x)
B = sp.diff(z, x, y)
C = sp.diff(z, y, y)

print("\n--- Аналіз точок ---")

for point in critical_points:
    x0, y0 = point

    val_A = A.subs({x: x0, y: y0})
    val_B = B.subs({x: x0, y: y0})
    val_C = C.subs({x: x0, y: y0})

    delta = val_A * val_C - val_B ** 2
    z_val = z.subs({x: x0, y: y0})

    print(f"Точка M({x0}, {y0}):")
    print(f"  A = {val_A}")
    print(f"  AC - B^2 = {delta}")

    if delta > 0:
        if val_A < 0:
            print(f"  Висновок: Локальний МАКСИМУМ. z_max = {z_val}")
        else:
            print(f"  Висновок: Локальний МІНІМУМ. z_min = {z_val}")
    elif delta < 0:
        print("  Висновок: Сідлова точка (екстремуму немає).")
    else:
        print("  Висновок: Сумнівний випадок (потрібні додаткові дослідження).")