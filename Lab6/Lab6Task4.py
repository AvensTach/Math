import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


sp.init_printing()
x, y = sp.symbols('x y')

f = x*y + 1

inner_integral = sp.integrate(f, (x, -1, 1/y))

inner_integral_simplified = sp.simplify(inner_integral)
print("Внутрішній інтеграл (по x):")
print(inner_integral_simplified)

I = sp.integrate(inner_integral_simplified, (y, 1, 2))

print("\nПодвійний інтеграл I:")
sp.pprint(I)

I_numerical = I.evalf()
print("\nЧислове значення I ≈")
sp.pprint(I_numerical)


y_vals = np.linspace(1, 2, 100)
x_curve = 1/y_vals
x_line = -1 * np.ones_like(y_vals)

plt.figure(figsize=(7, 7))

plt.plot(x_curve, y_vals, label=r'$x = \frac{1}{y}$', color='blue', linewidth=2)
plt.axvline(x=-1, ymin=0, ymax=1, label=r'$x = -1$', color='orange', linestyle='--', linewidth=2)
plt.axhline(y=1, xmin=-2, xmax=2, label=r'$y = 1$', color='red', linestyle=':', linewidth=2)
plt.axhline(y=2, xmin=-2, xmax=2, label=r'$y = 2$', color='green', linestyle='-.', linewidth=2)


x_fill = np.concatenate([x_line, x_curve[::-1]])
y_fill = np.concatenate([y_vals, y_vals[::-1]])

plt.fill(x_fill, y_fill, 'lightblue', alpha=0.7, label='Область D')

plt.xlim(-1.5, 1.5)
plt.ylim(0, 3)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Область інтегрування D')
plt.legend()
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()