import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x, y, r, theta = sp.symbols('x y r theta')

theta_start = 7 * sp.pi / 6
theta_end = 5 * sp.pi / 4
r_curve = -4 * sp.cos(theta)

area_polar = sp.integrate(sp.Rational(1, 2) * r_curve**2, (theta, theta_start, theta_end))


x_circle_left = -2 - sp.sqrt(4 - y**2)
x_line_1 = y             # x = y
x_line_2 = sp.sqrt(3)*y  # x = sqrt(3)y

S_cartesian_1 = sp.integrate(x_line_1 - x_circle_left, (y, -2, -sp.sqrt(3)))
S_cartesian_2 = sp.integrate(x_line_1 - x_line_2, (y, -sp.sqrt(3), 0))
area_cartesian = S_cartesian_1 + S_cartesian_2

print(f"Площа (Полярні): {area_polar}  (= {area_polar.evalf()})")
print(f"Площа (Декартові): {area_cartesian}  (= {area_cartesian.evalf()})")
print(f"Різниця: {sp.simplify(area_polar - area_cartesian)}")

if sp.simplify(area_polar - area_cartesian) == 0:
    print("ВІДПОВІДІ СПІВПАДАЮТЬ!")
else:
    print("Увага: є розбіжність.")


fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(121)

delta = 0.025
x_range = np.arange(-4.5, 0.5, delta)
y_range = np.arange(-2.5, 0.5, delta)
X, Y = np.meshgrid(x_range, y_range)

F_circle = X**2 + Y**2 + 4*X
F_line1 = Y - X
F_line2 = np.sqrt(3)*Y - X

ax1.contour(X, Y, F_circle, levels=[0], colors='red', linewidths=2) # Коло
ax1.contour(X, Y, F_line1, levels=[0], colors='blue', linewidths=2) # y=x
ax1.contour(X, Y, F_line2, levels=[0], colors='green', linewidths=2) # sqrt(3)y=x

region_mask = (F_circle <= 0) & (Y >= X) & (np.sqrt(3)*Y <= X)
ax1.imshow(region_mask.astype(int), extent=(x_range.min(), x_range.max(), y_range.min(), y_range.max()),
           origin='lower', cmap='Greys', alpha=0.3)

ax1.set_title('Область D (Декартова система)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)
ax1.set_aspect('equal')

ax1.plot([], [], color='red', label=r'$x^2+y^2+4x=0$')
ax1.plot([], [], color='blue', label=r'$y=x$')
ax1.plot([], [], color='green', label=r'$\sqrt{3}y=x$')
ax1.legend()

ax2 = fig.add_subplot(122, projection='polar')


theta_vals = np.linspace(0, 2*np.pi, 400)

r_vals = -4 * np.cos(theta_vals)

r_vals[r_vals < 0] = 0

ax2.plot(theta_vals, r_vals, color='red', label='$r=-4\cos\\theta$')

ax2.plot([5*np.pi/4, 5*np.pi/4], [0, 4], color='blue', label='$\\theta=5\pi/4$')
ax2.plot([7*np.pi/6, 7*np.pi/6], [0, 4], color='green', label='$\\theta=7\pi/6$')

theta_fill = np.linspace(7*np.pi/6, 5*np.pi/4, 100)
r_fill = -4 * np.cos(theta_fill)
ax2.fill_between(theta_fill, 0, r_fill, color='gray', alpha=0.5)

ax2.set_title('Область D (Полярна система)')
ax2.set_ylim(0, 4)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()