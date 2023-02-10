def falling(n, k):
    d = n
    if k == 0:
        return 1
    for i in range(1, k):
        d = d - 1
        n *= d
    return n
print(falling(6, 3))