import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Репета-3 ст. 95 № 3.1.29

sp.init_printing(use_unicode=True)


x = sp.symbols('x')
n = sp.symbols('n', integer=True)

f_expr = 3*x - 5

a0_int = sp.integrate(f_expr, (x, 0, sp.pi))
a0 = (1/sp.pi) * a0_int

an_int = sp.integrate(f_expr * sp.cos(n*x), (x, 0, sp.pi))
an = (1/sp.pi) * an_int

an = sp.simplify(an.rewrite(sp.cos))

bn_int = sp.integrate(f_expr * sp.sin(n*x), (x, 0, sp.pi))
bn = (1/sp.pi) * bn_int
bn = sp.simplify(bn.rewrite(sp.cos))

print("--- Коефіцієнти ряду Фур'є ---")
print(f"a0 = {a0}")
print(f"an = {an}")
print(f"bn = {bn}")

k_max = 10
fourier_series = a0 / 2
for i in range(1, k_max + 1):
    coef_a = an.subs(n, i)
    coef_b = bn.subs(n, i)
    fourier_series += coef_a * sp.cos(i*x) + coef_b * sp.sin(i*x)



f_numeric_original = sp.lambdify(x, f_expr, "numpy")
f_numeric_series = sp.lambdify(x, fourier_series, "numpy")

x_vals = np.linspace(-np.pi, np.pi, 400)

y_vals_original = np.piecewise(x_vals,
                               [x_vals < 0, x_vals >= 0],
                               [0, lambda x: 3*x - 5])

y_vals_series = f_numeric_series(x_vals)

plt.figure(figsize=(10, 6))

# Малюємо оригінал
plt.plot(x_vals, y_vals_original, 'k--', linewidth=2, label='f(x) Оригінал')

# Малюємо апроксимацію рядом Фур'є
plt.plot(x_vals, y_vals_series, 'r', linewidth=1.5, label=f'Ряд Фур\'є (n={k_max})')

plt.title("Розклад функції в ряд Фур'є")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()

print('-'*30)

# Репета-3 ст. 30 № 1.1.29

sp.init_printing(use_unicode=True)

n = sp.symbols('n')

a_n = 1 / ((3*n + 5) * (3*n + 2))

total_sum = sp.summation(a_n, (n, 1, sp.oo))

print("--- Загальний член ряду ---")
sp.pprint(a_n)

print("\n--- Сума ряду ---")
sp.pprint(total_sum)