from collections import deque
def bfs(maps, sx, sy, ex, ey):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    isvisited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    isvisited[sx][sy] = 0
    while q:
        x, y = q.popleft()
        if (x, y) == (ex, ey):
            return isvisited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if isvisited[nx][ny]: continue
            if maps[nx][ny] == 'X': continue
            isvisited[nx][ny] = isvisited[x][y] + 1
            q.append((nx, ny))
    return 0

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                startx, starty = i, j
            elif maps[i][j] == 'E':
                exitx, exity = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
    l_dis = bfs(maps, startx, starty, lx, ly)
    if l_dis == 0:
        return -1
    end_dis = bfs(maps, lx, ly, exitx, exity)
    return end_dis + l_dis if end_dis != 0 else -1