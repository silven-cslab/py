# Q22: Add, transpose and multiply two matrices (without NumPy)

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

n = len(A)
m = len(A[0])


def show(title, M):
    print(title)
    for row in M:
        print(row)
    print()


show("Matrix A:", A)
show("Matrix B:", B)

# Addition
add = [[A[i][j] + B[i][j] for j in range(m)] for i in range(n)]
show("A + B:", add)

# Transpose
transpose = [[A[i][j] for i in range(n)] for j in range(m)]
show("Transpose of A:", transpose)

# Multiplication
mul = [[0] * len(B[0]) for _ in range(n)]
for i in range(n):
    for j in range(len(B[0])):
        for k in range(len(B)):
            mul[i][j] += A[i][k] * B[k][j]
show("A x B:", mul)
