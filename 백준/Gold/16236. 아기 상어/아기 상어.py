from collections import deque
import sys
input = sys.stdin.readline
def eat_fish(sx, sy, distance, Map):
    global size, eat, time
    Map[sx][sy] = 0
    fish_far = 10000
    x, y = -1, -1
    for i in range(n):
        for j in range(n):
            if 0 < Map[i][j] < size and 0 < distance[i][j] < fish_far:
                fish_far = distance[i][j]
                x, y = i, j
    if x == -1 and y == -1: return
    Map[x][y] = 9
    eat += 1
    time += distance[x][y]
    if size == eat:
        size += 1
        eat = 0


def check_dis(sx, sy):
    q = deque()
    q.append([sx, sy])
    distance = [[-1] * n for _ in range(n)]
    distance[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if distance[nx][ny] != -1: continue
            if Map[nx][ny] > size: continue
            distance[nx][ny] = distance[x][y] + 1
            q.append([nx, ny])
    return distance

n = int(input())
size = 2
eat = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Map = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
play = False
for i in range(n):
    for j in range(n):
        if 0 < Map[i][j] < size:
            cnt += 1
        if Map[i][j] == 9:
            start = [i, j]
if cnt >= 1:
    play = True
distance = check_dis(start[0], start[1])
time = 0
while play:
    cnt = 0
    eat_fish(start[0], start[1], distance, Map)
    for i in range(n):
        for j in range(n):
            if 0 < Map[i][j] < size and Map[i][j] != 9:
                cnt += 1
            if Map[i][j] == 9:
                start = [i, j]
    if cnt >= 1:
        play = True
    else:
        play = False
    distance = check_dis(start[0], start[1])
    for i in Map:
        if 9 in i:
            play = True
            break
        else:
            play = False
print(time)
