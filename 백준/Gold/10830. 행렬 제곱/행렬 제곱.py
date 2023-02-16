import sys
input = sys.stdin.readline
def multi(A, B):
    temp = [[0 for _ in range(len(A))] for _ in range(len(B[0]))]
    for k in range(n):
        for i in range(len(A[0])):
            for j in range(len(B[0])):
                temp[k][i] += A[k][j] * B[j][i]
            temp[k][i] %= 1000
    return temp
def multi_check(A, n):
    if n == 1:
        for i in range(n + 1):
            for j in range(n + 1):
                A[i][j] %= 1000
        return A
    tmp = multi_check(A, n // 2)
    if n % 2:
        return multi(multi (tmp, tmp), A)
    else:
        return multi(tmp, tmp)

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = multi_check(matrix, b)
for row in result: print(*row)