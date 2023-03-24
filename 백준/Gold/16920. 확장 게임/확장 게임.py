from collections import deque
n, m, p = map(int, input().split())
move = [0] + list(map(int, input().split()))
Map = [list(input()) for _ in range(n)]
cnt = [0] * (p + 1)

# 4방 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs
country = [deque() for _ in range(p + 1)]
for i in range(n):
    for j in range(m):
        if Map[i][j] != '.' and Map[i][j] != '#':
            country[int(Map[i][j])].append((i, j))
            cnt[int(Map[i][j])] += 1
is_moved = True
while is_moved:
    is_moved = False
    for i in range(1, p + 1):
        if not country[i]:
            continue
        q = country[i]
        for _ in range(move[i]):
            if not q:
                break
            for _ in range(len(q)):
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if not(0 <= nx < n and 0 <= ny < m): continue
                    if Map[nx][ny] != '.': continue
                    Map[nx][ny] = str(i)
                    q.append((nx, ny))
                    cnt[i] += 1
                    is_moved = True

print(*cnt[1:])