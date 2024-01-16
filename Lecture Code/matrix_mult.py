# O(n^3) matrix multiplication
def strassen(A,B,n):
    C = [[]]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C

# Theta(n^3) matrix multiplication
def divideconquer(A,B,n):
    C = [[]]
    if n == 1:
        C[0][0] = A[0][0]*B[0][0]
    else:
        C[0][0] = divideconquer(A[0][0],B[0][0],n/2) + divideconquer(A[0][1],B[1][0],n/2)
        C[0][1] = divideconquer(A[0][0],B[0][1],n/2) + divideconquer(A[0][1],B[1][1],n/2)
        C[1][0] = divideconquer(A[1][0],B[0][0],n/2) + divideconquer(A[1][1],B[1][0],n/2)
        C[1][1] = divideconquer(A[1][0],B[0][1],n/2) + divideconquer(A[1][1],B[1][1],n/2)
    return C
