import sympy as sp
sp.init_printing()
t = sp.Symbol('t')
x = sp.Function('x')
y = sp.Function('y')

x_dot = x(t).diff(t)
y_dot = y(t).diff(t)

eq1 = sp.Eq(x_dot, -3*x(t) - y(t) - sp.exp(-2*t))

eq2 = sp.Eq(y_dot, x(t) - y(t) + 1)

system_of_eqs = [eq1, eq2]

solution = sp.dsolve(system_of_eqs, [x(t), y(t)])

print("Символьний розв'язок системи диференціальних рівнянь:")
print("-" * 55)
for sol_eq in solution:
    sp.pprint(sol_eq)