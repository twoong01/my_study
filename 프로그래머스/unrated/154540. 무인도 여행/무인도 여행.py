from collections import deque
def bfs(isvisited, sx, sy, maps):
    n = len(maps)
    m = len(maps[0])
    total = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((sx, sy))
    total += int(maps[sx][sy])
    isvisited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if isvisited[nx][ny]: continue
            if maps[nx][ny] == 'X': continue
            q.append((nx, ny))
            total += int(maps[nx][ny])
            isvisited[nx][ny] = True
    return total

def solution(maps):
    answer = []
    
    n = len(maps)
    m = len(maps[0])
    isvisited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not isvisited[i][j]:
                answer.append(bfs(isvisited, i, j, maps))
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer