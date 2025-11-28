q = lambda l: q([x for x in l[:-1] if x <= l[-1]]) + [l[-1]] + q([x for x in l[:-1] if x > l[-1]]) if len(l) > 0 else []

shuffled_test = [1, 235, 2, 9, 1, 6, 7, 23, 6, 78, 56, 4, 7, 9, 7]
print(q(shuffled_test))

def power(x:int, y:int) -> int:
    return x**y


power