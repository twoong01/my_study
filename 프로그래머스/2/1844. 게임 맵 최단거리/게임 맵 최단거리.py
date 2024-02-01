from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append([0, 0, 1])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    while q:
        x, y, cnt = q.popleft()
        if (x + 1, y + 1) == (n, m):
            return cnt
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if visited[nx][ny]: continue
            if not maps[nx][ny]: continue
            q.append([nx, ny, cnt + 1])
            visited[nx][ny] = True
    return -1