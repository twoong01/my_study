n = int(input())
maps = [list(input()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
num = []

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if maps[x][y] == '1':
        global cnt
        cnt += 1
        maps[x][y] = '0'
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

cnt = 0
for i in range(n):
    for j in range(n):
        if maps[i][j] != '0':
            if dfs(i, j):
                num.append(cnt)
                cnt = 0

num.sort()
print(len(num))
for i in range(len(num)):
    print(num[i])