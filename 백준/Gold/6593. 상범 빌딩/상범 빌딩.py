from collections import deque


while True:
    L, R, C = map(int, input().split())
    if L + R + C == 0:
        break
    buliding = [[[] * C for _ in range(R)] for _ in range(L)]
    for k in range(L):
        buliding[k] = [list(input().rstrip()) for _ in range(R)]
        input()
    q = deque()
    isvisited = [[[False] * C for _ in range(R)] for _ in range(L)]
    for floor in range(L):
        for i in range(R):
            for j in range(C):
                if buliding[floor][i][j] == 'S':
                    q.append([floor, i, j])
                    isvisited[floor][i][j] = 0


    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    while q:
        z, x, y = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if not(0 <= nx < R and 0 <= ny < C and 0 <= nz < L): continue
            if isvisited[nz][nx][ny] != False: continue
            if buliding[nz][nx][ny] == '#': continue
            q.append([nz, nx, ny])
            isvisited[nz][nx][ny] = isvisited[z][x][y] + 1
    escape = 0
    for z in range(L):
        for i in range(R):
            for j in range(C):
                if isvisited[z][i][j] != False:
                    if buliding[z][i][j] == 'E':
                        print(f'Escaped in {isvisited[z][i][j]} minute(s).')
                        escape = 1
    else:
        if not escape:
            print('Trapped!')