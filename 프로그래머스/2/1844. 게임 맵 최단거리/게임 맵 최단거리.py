from collections import deque
def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append([0, 0, 1])
    while q:
        x, y, step = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return step
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if maps[nx][ny] == 0: continue
            q.append([nx, ny, step + 1])
            maps[nx][ny] = 0
    return -1
            