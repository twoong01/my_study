from collections import deque
N, M = map(int, input().split())
box = []
tomato = []
for i in range(M):
    box.append(list(map(int, input().split())))
    for j in range(N):
        if box[i][j] == 1:
            tomato.append([0, i, j])
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

queue = deque(tomato)
while queue:
    day, x, y = queue.popleft()
    for i in range(4):
        ni = x + di[i]
        nj = y + dj[i]
        if 0 <= ni < M and 0 <= nj < N and box[ni][nj] == 0:
            box[ni][nj] = 1
            queue.append([day + 1, ni, nj])
for i in range(M):
    if 0 in box[i]:
        print(-1)
        break
else:
    print(day)