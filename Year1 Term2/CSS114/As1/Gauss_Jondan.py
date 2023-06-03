def gauss_jordan(A, b):

    # Gauss-Jordan Method [By Bottom Science]
    n = len(A)
    M = A

    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k+1, n):
            q = M[j][k] / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] = M[n-1][n] / M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z  + M[i][j]*x[j]
        x[i] = (M[i][n] - z) / M[i][i]
    return x

# A - coefficient matrix
A = [[1, 4, 9], [4, 9, 16], [9, 16, 25]]
b = [10, 14, 18]
print(gauss_jordan(A, b))

# Output - [6.0, -1.0, -2.0]