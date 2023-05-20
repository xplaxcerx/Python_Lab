#include <stdio.h>
#include <math.h>

double f(double x) {
    return cos(sqrt(x)) - x;
}

double g(double x) {
    return cos(x) / sqrt(1 + x);
}

int main() {
    int n = 10;
    int m = 10;
    double A[10][10];
    double B[10][10];

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            A[i][j] = f(i + 1) + g(j + 1);
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            B[i][j] = A[n - 1 - j][m - 1 - i];
        }
    }

    double result_matrix[10][10];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            result_matrix[i][j] = 0;
            for (int k = 0; k < m; k++) {
                result_matrix[i][j] += B[i][k] * A[k][j];
            }
        }
    }

    double T = 100000;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (result_matrix[i][j] < T) {
                T = fabs(result_matrix[i][j]);
            }
        }
    }
    printf("%lf\n", sqrt(T));

    return 0;
}
