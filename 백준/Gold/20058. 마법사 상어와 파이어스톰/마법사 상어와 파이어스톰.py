import copy
from collections import deque
def rotate(size):
    rotated = [[0] * (2**N) for _ in range(2**N)]
    for y in range(0, 2**N, size):
        for x in range(0, 2**N, size):
            for i in range(size):
                for j in range(size):
                    rotated[y + j][x + size - i - 1] = maps[y + i][x + j]
    return rotated

def melt():
    tmp = copy.deepcopy(maps)
    q = deque()
    for i in range(2**N):
        for j in range(2**N):
            if not maps[i][j]: continue
            q.append((i, j))
            cnt = 0
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not(0 <= nx < 2**N and 0 <= ny < 2**N): continue
                    if not maps[nx][ny]: continue
                    cnt += 1
            if cnt < 3:
                tmp[i][j] -= 1
    return tmp
def check_iceberg():
    q = deque()
    isvisited = [[False] * (2**N) for _ in range(2**N)]
    mx = 0
    for i in range(2**N):
        for j in range(2**N):
            if not maps[i][j]: continue
            if isvisited[i][j]: continue
            cnt = 1
            q.append((i, j))
            isvisited[i][j] = True
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not(0 <= nx < 2**N and 0 <= ny < 2**N): continue
                    if isvisited[nx][ny]: continue
                    if not maps[nx][ny]: continue
                    q.append((nx, ny))
                    isvisited[nx][ny] = True
                    cnt += 1
            mx = max(mx, cnt)
    return mx

N, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(2**N)]
L_lst = list(map(int, input().split()))
total = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for L in L_lst:
    box_size = 2**L
    maps = rotate(box_size)
    maps = melt()
mx = check_iceberg()
for i in range(2**N):
    total += sum(maps[i])
print(total)
print(mx)