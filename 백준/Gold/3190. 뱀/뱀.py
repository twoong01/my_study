from collections import deque
n = int(input())
k = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = [[0] * n for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2
l = int(input())
dirDict = dict()
q = deque()
q.append((0, 0))
for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
time = 0
direction = 0

def turn(alpha):
    global direction
    if alpha == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction + 3) % 4

while q:
    time += 1
    x = x + dx[direction]
    y = y + dy[direction]

    if not(0 <= x < n and 0 <= y < n):
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        q.append((x, y))
        if time in dirDict:
            turn(dirDict[time])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        q.append((x, y))
        nx, ny = q.popleft()
        graph[nx][ny] = 0
        if time in dirDict:
            turn(dirDict[time])
    else:
        break
print(time)