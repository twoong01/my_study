from collections import deque
r, c, t = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(r)]

def spread():
    dust = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(r):
        for j in range(c):
            if house[i][j] > 0:
                d = int(house[i][j] / 5)
                dust.append([i, j, d])

    while dust:
        x, y, d = dust.popleft()
        cnt = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < r and 0 <= ny < c): continue
            if house[nx][ny] == -1: continue
            house[nx][ny] += d
            cnt += 1
        house[x][y] -= d * cnt

for time in range(t):
    spread()
    # 공기청정기 작동
    count = 0
    for i in range(r):
        for j in range(c):
            if house[i][j] == -1 and count == 0:
                # 오른쪽으로 밀기
                a = house[i].pop()
                house[i].insert(1, 0)
                # 위로 밀기
                for row in range(1, i + 1):
                    house[i - row].append(a)
                    a = house[i - row].pop(-2)
                # 왼쪽으로 밀기
                house[0].insert(-1, a)
                a = house[0].pop(0)
                for row in range(1, i):
                    house[row].insert(0, a)
                    a = house[row].pop(1)
                count = 1
            elif house[i][j] == -1 and count == 1:
                # 오른쪽으로 밀기
                a = house[i].pop()
                house[i].insert(1, 0)
                # 밑으로 밀기
                for row in range(1, r-i):
                    house[i + row].append(a)
                    a = house[i + row].pop(-2)
                # 왼쪽으로 밀기
                house[r-1].insert(-1, a)
                a = house[r-1].pop(0)
                for row in range(r-2, i, -1):
                    house[row].insert(0, a)
                    a = house[row].pop(1)
                count = 0
total = 0
for i in house:
    total += sum(i)
print(total + 2)