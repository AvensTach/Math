import matplotlib
matplotlib.use('TkAgg')

import sympy as sp
from sympy.plotting import plot, plot_implicit, plot3d, plot_backends


# Ініціалізація
x, y, z = sp.symbols('x y z')


# 1. Побудова кривої y = (x^2 - 1) / x

print("Будуємо графік №1...")
f = (x**2 - 1) / x

p1 = plot(f, (x, -10, -0.1), show=False, line_color='blue', title="Завдання 1: y = (x^2 - 1)/x")
p1_part2 = plot(f, (x, 0.1, 10), show=False, line_color='blue')
p1.append(p1_part2[0])
p1.ylim = (-10, 10)
p1.show()



# 2. Неявні криві в одному вікні

print("Будуємо графік №2 (неявні функції)...")

# Рівняння 1: Еліпс 36x^2 + 25y^2 - 900 = 0
eq1 = sp.Eq(36*x**2 + 25*y**2 - 900, 0)

# Рівняння 2: x = -7/9 * sqrt(80 - 2y - y^2)
eq2 = sp.Eq(x + (sp.Rational(7, 9) * sp.sqrt(80 - 2*y - y**2)), 0)

plot_imp_1 = plot_implicit(eq1, (x, -10, 10), (y, -10, 10),
                           line_color='blue', show=False,
                           title="Завдання 2: Неявні криві")

plot_imp_2 = plot_implicit(eq2, (x, -10, 10), (y, -10, 10),
                           line_color='red', show=False)

plot_imp_1.append(plot_imp_2[0])
plot_imp_1.show()



# 3. Кольорова поверхня 4x^2 - y^2 + 4y - 4z + 4 = 0

print("Будуємо графік №3 (3D поверхня)...")

# Виражаємо z через x та y
z_func = sp.solve(4*x**2 - y**2 + 4*y - 4*z + 4, z)[0]

print(f"Рівняння для поверхні: z = {z_func}")

plot3d(z_func, (x, -5, 5), (y, -5, 10),
       title="Завдання 3: Поверхня z(x,y)",
       xlabel='X', ylabel='Y', zlabel='Z')