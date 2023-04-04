from collections import deque
def solution(maps):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    isvisited = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0))
    isvisited[0][0] = 1
    while q:
        x, y = q.popleft()
        if (x, y) == (n - 1, m - 1):
            return isvisited[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if maps[nx][ny] == 0: continue
            if isvisited[nx][ny] != -1: continue
            isvisited[nx][ny] = isvisited[x][y] + 1
            q.append((nx, ny))
    return -1