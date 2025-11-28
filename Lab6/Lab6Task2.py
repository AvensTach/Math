import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

sp.init_printing()

x = sp.Symbol('x')
y = sp.Function('y')

lhs = y(x).diff(x, 2) - 4 * y(x).diff(x)
rhs = 2*x**2 + 3*x - 1
ode = sp.Eq(lhs, rhs)

general_solution = sp.dsolve(ode, y(x))

print("а) Загальний розв'язок y(x):")
sp.pprint(general_solution)


ic_y = {y(0): 6}

ic_dy = {y(x).diff(x).subs(x, 0): -2}

ics = {**ic_y, **ic_dy}

particular_solution = sp.dsolve(ode, y(x), ics=ics)

print("\nб) Частковий розв'язок y(x) із початковими умовами:")
sp.pprint(particular_solution)


y_expr = particular_solution.rhs

y_func = sp.lambdify(x, y_expr, 'numpy')

x_vals = np.linspace(-2, 2, 400)
y_vals = y_func(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label=f'$y(x) = {sp.latex(y_expr)}$', color='blue')
plt.title('Графік часткового розв\'язку $y\'\' - 4y\' = 2x^2 + 3x - 1$', fontsize=14)
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y(x)$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()

plt.show()