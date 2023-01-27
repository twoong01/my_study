n, m = map(int, input().split())
lst1 = []
lst2 = []
for i in range(n):
    lst1.append(list(map(int, input().split())))

for i in range(n):
    lst2.append(list(map(int, input().split())))

ans = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        ans[i][j] = lst1[i][j] + lst2[i][j]

for i in range(n):
    print(*ans[i])