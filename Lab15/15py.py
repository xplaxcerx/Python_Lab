from math import *

n = 10
m = 10

f = lambda x: cos(sqrt(x)) - x
g = lambda x: cos(x) / sqrt(1 + x)

A = [[f(i) + g(j) for j in range (1, n + 1)] for i in range(1, m + 1)]
B = [[0 for i in range(n)] for i in range(m)]

for i in range(n):
    for j in range(m):
        B[i][j] = A[n-1-j][m-1-i]

result_matrix = [[sum(a * b for a, b in zip(Arow, Bcol)) for Bcol in zip(*A)] for Arow in B]

T = 100000
for i in range(n):
    for j in range(m):
        if result_matrix[i][j] < T:
            T = abs(result_matrix[i][j])
print(sqrt(T))