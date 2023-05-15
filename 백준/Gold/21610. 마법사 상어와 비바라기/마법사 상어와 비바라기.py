from collections import deque

def make_clouds():
    tmp = deque()
    for i in range(n):
        for j in range(n):
            if maps[i][j] < 2: continue
            if is_visited[i][j]: 
                is_visited[i][j] = False
                continue
            maps[i][j] -= 2
            tmp.append([i, j])
    return tmp


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
clouds = [list(map(int, input().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

check_dx = [-1, -1, 1, 1]
check_dy = [-1, 1, -1, 1]

clouds_xy = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

is_visited = [[False] * n for _ in range(n)]

for i in clouds:
    direction, repeat = i[0], i[1]
    for j in range(len(clouds_xy)):
        x, y = clouds_xy.popleft()
        nx = (x + dx[direction - 1] * repeat) % n
        ny = (y + dy[direction - 1] * repeat) % n
        clouds_xy.append([nx, ny])
        maps[nx][ny] += 1
    
    for j in clouds_xy:
        x, y = j[0], j[1]
        is_visited[x][y] = True
        total = 0
        for k in range(4):
            nx = x + check_dx[k]
            ny = y + check_dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if maps[nx][ny] == 0: continue
            total += 1
        maps[x][y] += total
    clouds_xy = make_clouds()
total = 0

for i in range(n):
    for j in range(n):
        total += maps[i][j]
print(total)