n = int(input())
level = []
for i in range(n):
    level.append(int(input()))
cnt = 0
for i in range(n-1, 0, -1):
    if level[i] <= level[i-1]:
        cnt += (level[i-1]-level[i]+1)
        level[i-1] = level[i] - 1
print(cnt)