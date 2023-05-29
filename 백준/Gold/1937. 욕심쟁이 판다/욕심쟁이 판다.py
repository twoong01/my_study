import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(i, j):
    if is_visited[i][j]:
        return is_visited[i][j]

    is_visited[i][j] = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if not(0 <= nx < n and 0 <= ny < n): continue
        if maps[nx][ny] > maps[i][j]:
            is_visited[i][j] = max(is_visited[i][j], dfs(nx, ny) + 1)
    return is_visited[i][j]
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
ans = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
is_visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dfs(i, j)

for i in range(n):
    ans = max(ans, max(is_visited[i]))
print(ans)