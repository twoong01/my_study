from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    tmp.append([x, y])
    while q:
        a, b = q.popleft()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and Map[nx][ny] == Map[x][y] and isvisited[nx][ny] == 0:
                q.append((nx, ny))
                tmp.append((nx, ny))
                isvisited[nx][ny] = 1
def delete(tmp):
    for x, y in tmp:
        Map[x][y] = '.'

def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, - 1):
                if Map[j][i] != '.' and Map[k][i] == '.':
                    Map[k][i] = Map[j][i]
                    Map[j][i] = '.'
                    break

Map = [list(input()) for _ in range(12)]
total = 0
start = [11, 0]
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

while True:
    flag = 0
    isvisited = [[0 for _ in range(6)] for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if Map[i][j] != '.' and isvisited[i][j] == 0:
                isvisited[i][j] = 1
                tmp = []
                bfs(i, j)
                if len(tmp) >= 4:
                    flag = 1
                    delete(tmp)
    if flag == 0:
        break
    down()
    total += 1
print(total)