from collections import deque

m, n, h = map(int, input().split())
box = []
tomato = []
for i in range(h):
    box.append([])
    for j in range(n):
        box[i].append(list(map(int, input().split())))
        for k in range(m):
            if box[i][j][k] == 1:
                tomato.append([0, i, j, k])
di = [-1, 1, 0, 0, 0, 0] # 좌우앞뒤위아래
dj = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


q = deque(tomato)
while q:
    day, z, y, x = q.popleft()
    for i in range(6):
        ni = x + di[i]
        nj = y + dj[i]
        nz = z + dz[i]
        if 0 <= ni < m and 0 <= nj < n and 0<= nz < h and box[nz][nj][ni] == 0:
            box[nz][nj][ni] = 1
            q.append([day + 1, nz, nj, ni])

for i in range(h):
    for j in range(n):
        if 0 in box[i][j]:
            print(-1)
            exit()
else:
    print(day)