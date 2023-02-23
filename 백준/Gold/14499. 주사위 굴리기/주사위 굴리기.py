from collections import deque
n, m, x, y, k = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
order = deque(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0] * 6
if box[x][y] != 0:
    dice[5] = box[x][y]
    box[x][y] = 0

def moveEast():
    dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    print(dice[0])
    return

def moveWest():
    dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    print(dice[0])
    return

def moveNorth():
    dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    print(dice[0])
    return

def moveSouth():
    dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    print(dice[0])
    return

while order:
    move = order.popleft()
    nx = x + dx[move - 1]
    ny = y + dy[move - 1]
    if not(0 <= nx < n and 0 <= ny < m):
        continue
    if move == 1:
        moveEast()
    elif move == 2:
        moveWest()
    elif move == 3:
        moveNorth()
    else:
        moveSouth()

    if box[nx][ny] == 0:
        box[nx][ny] = dice[5]
    else:
        dice[5] = box[nx][ny]
        box[nx][ny] = 0
    x, y = nx, ny