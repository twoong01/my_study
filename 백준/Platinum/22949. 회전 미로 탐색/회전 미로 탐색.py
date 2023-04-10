from collections import deque

# getDivision 함수 구현
def getDivision(r, c):
    if r < 0 or c < 0 or r >= 4*n or c >= 4*n:
        return -1
    return r // 4 * 4 + c // 4

# getRotatedPos 함수 구현
def getRotatedPos(r, c):
    baseR = r // 4 * 4
    baseC = c // 4 * 4
    r %= 4
    c %= 4
    return (baseR + c, baseC + 3 - r)

# 입력 처리
n = int(input())
arr = [[['#' for _ in range(4*n)] for _ in range(4*n)] for _ in range(4)]
start = None
for i in range(4*n):
    row = input().strip()
    for j in range(4*n):
        c = row[j]
        arr[0][i][j] = c
        if c == 'S':
            start = (i, j, 0, 0)
        tmpI, tmpJ = i, j
        for x in range(1, 4):
            nextPos = getRotatedPos(tmpI, tmpJ)
            tmpI, tmpJ = nextPos
            arr[x][tmpI][tmpJ] = c

# bfs 탐색
dr = [0, 1, -1, 0, 0]
dc = [0, 0, 0, 1, -1]
visited = [[[False] * (4*n) for _ in range(4*n)] for _ in range(4)]
q = deque()
q.append(start)
visited[start[2]][start[0]][start[1]] = True
while q:
    r, c, d, dist = q.popleft()
    if arr[d][r][c] == 'E':
        print(dist)
        break
    cDiv = getDivision(r, c)
    for dir in range(5):
        nr = r + dr[dir]
        nc = c + dc[dir]
        nDiv = getDivision(nr, nc)
        if nDiv == -1:
            continue
        nd = (d + 1) % 4 if cDiv == nDiv else 1
        nrc = getRotatedPos(nr, nc)
        nr, nc = nrc
        if visited[nd][nr][nc] or arr[nd][nr][nc] == '#':
            continue
        visited[nd][nr][nc] = True
        q.append((nr, nc, nd, dist + 1))
else:
    print(-1)
