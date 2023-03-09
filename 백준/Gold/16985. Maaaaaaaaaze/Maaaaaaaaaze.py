Maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
b = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
ans = 1e9

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

from collections import deque
from itertools import permutations
def bfs(b):
    global ans
    isvisited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    start = [0, 0, 0]
    q = deque([start])

    while q:
        z, y, x = q.popleft()

        if z == 4 and y == 4 and x == 4:
            ans = min(ans, isvisited[z][y][x])
            if ans == 12:
                print(ans)
                exit()
            return

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if not (0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5): continue
            if isvisited[nz][ny][nx] != 0 or b[nz][ny][nx] == 0: continue
            isvisited[nz][ny][nx] = isvisited[z][y][x] + 1
            q.append((nz, ny, nx))


def rotate(b):
    global Maze
    tmp = [[0] * 5 for _ in range(5)]
    for i in range(len(b)):
        for j in range(len(b[0])):
            tmp[j][4 - i] = b[i][j]
    return tmp

def dfs(i):
    global b
    if i == 5:
        if b[4][4][4]:
            bfs(b)
        return
    for _ in range(4):
        if b[0][0][0]:
            dfs(i + 1)
        b[i] = rotate(b[i])


for order in permutations([0, 1, 2, 3, 4]):
    for i in order:
        b[order[i]] = Maze[i]
    dfs(0)

print(ans if ans != 1e9 else -1)