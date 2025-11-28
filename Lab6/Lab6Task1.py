import sympy as sp

sp.init_printing()

x = sp.Symbol('x')
y = sp.Function('y')


lhs = y(x).diff(x, 2) - 3 * y(x).diff(x) + 2 * y(x)

rhs = sp.exp(2*x)

ode = sp.Eq(lhs, rhs)
print("Диференціальне рівняння:")
print(ode)
print("-" * 30)

solution = sp.dsolve(ode, y(x))

print("Символьний розв'язок y(x):")
sp.pprint(solution)