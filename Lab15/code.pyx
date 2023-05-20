from libc.math cimport cos, sqrt
import numpy as np

cdef double f(double x) nogil:
    return cos(sqrt(x)) - x

cdef double g(double x) nogil:
    return cos(x) / sqrt(1 + x)

cpdef double calculate_sqrt():
    cdef int n = 10
    cdef int m = 10

    cdef double[:, :] A = np.zeros((n, m), dtype=np.float64)
    cdef double[:, :] B = np.zeros((m, n), dtype=np.float64)

    cdef int i, j
    for i in range(n):
        for j in range(m):
            B[i, j] = A[n-1-j, m-1-i]

    cdef double[:, :] result_matrix = np.zeros((n, m), dtype=np.float64)
    cdef int k
    for i in range(n):
        for j in range(m):
            result_matrix[i, j] = 0
            for k in range(n):
                result_matrix[i, j] += A[i, k] * B[k, j]

    cdef double T = 100000
    for i in range(n):
        for j in range(m):
            if result_matrix[i, j] < T:
                T = abs(result_matrix[i, j])
    return sqrt(T)
