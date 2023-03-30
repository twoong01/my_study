import sys
input = sys.stdin.readline
def dfs(i, j, hp, mint_cnt):
    global cnt

    for nx, ny in mint:
        if Map[nx][ny] == 2:
            d = abs(i - nx) + abs(j - ny)
            if d <= hp:
                Map[nx][ny] = 0
                dfs(nx, ny, hp + h - d, mint_cnt + 1)
                Map[nx][ny] = 2
    
    if abs(i - start_x) + abs(j - start_y) <= hp:
        cnt = max(cnt, mint_cnt)

n, m, h = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
mint = []
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1:
            start_x, start_y = i, j
        if Map[i][j] == 2:
            mint.append([i, j ])
cnt = 0
dfs(start_x, start_y, m, 0)
print(cnt)
