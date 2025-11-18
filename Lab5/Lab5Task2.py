import sympy as sp

# Репета-2 ст. 72-74 № 1.3.29

sp.init_printing(use_unicode=True)

z = sp.symbols('z')

equation = z**6 + 4096

roots = sp.solve(equation, z)

print(f"Знайдено {len(roots)} коренів для z^6 = -4096:")
print("-" * 30)

for i, root in enumerate(roots):
    print(f"z_{i} = {sp.simplify(root)}")