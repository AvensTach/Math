import sympy as sp
import pprint
M = sp.Matrix([
    [1, -1, 1, -1, -2],
    [1, 2, -2, -1, -5],
    [2, -1, -3, 2, -1],
    [1, 2, 3, -6, -10]
])


A_rank = M[:, :4].rank()

M_rank = M.rank()

print(f"Rank of A: {A_rank}")
print(f"Rank of (A|b): {M_rank}")

# Check for consistency
if A_rank == M_rank:
    print("\nThe system is consistent.")
    # Define variables
    x1, x2, x3, x4 = sp.symbols('x1, x2, x3, x4')

    # Solve the system
    solution = sp.linsolve(M, [x1, x2, x3, x4])

    print("\nGeneral solution:")
    print(solution)
else:
    print("\nThe system is inconsistent.")