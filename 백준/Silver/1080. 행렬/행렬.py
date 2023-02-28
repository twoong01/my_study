n, m = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(n)]
B = [list(map(int, list(input()))) for _ in range(n)]
cnt = 0

def convert(start, array):
    x, y = start
    for i in range(x, x+3):
        for j in range(y, y+3):
            array[i][j] = 1 - array[i][j]
for i in range(0, n-2):
    for j in range(0, m-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            convert((i, j), A)
flag = 0
for i in range(n):
    if A[i] != B[i]:
        print(-1)
        flag = 1
        break
if flag == 0:
    print(cnt)