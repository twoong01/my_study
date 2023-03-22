def dfs(i, j):
    if i == n - 1 and j == m - 1:
        return 1

    if ans[i][j] != -1:
        return ans[i][j]

    ways = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and Map[nx][ny] < Map[i][j]:
            ways += dfs(nx, ny)

    ans[i][j] = ways
    return ans[i][j]

n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(0, 0))