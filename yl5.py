import itertools

def equiv(a, b):
    return a == b

print("A B C | A AND (B OR C) | (A ~ B) OR NOT(C AND A)")
print("-"*55)

for A, B, C in itertools.product([False, True], repeat=3):
    expr1 = A and (B or C)
    expr2 = equiv(A, B) or (not (C and A))
    print(A, B, C, "|", expr1, "|", expr2)
