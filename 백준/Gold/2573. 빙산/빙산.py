from collections import deque

def melt(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while q:
        x, y = q.popleft()
        sea = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if not Map[nx][ny]:
                sea += 1
            elif Map[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
        if sea > 0:
            seaList.append((x, y, sea))
    for x, y, sea in seaList:
        Map[x][y] = max(0, Map[x][y] - sea)
    return 1


n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

ice = []
for i in range(n):
    for j in range(m):
        if Map[i][j]:
            ice.append((i, j))  # 빙산의 위치를 (i, j) 형태로 ice에 저장

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0

while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if Map[i][j] and not visited[i][j]:
            group += melt(i, j)
        if Map[i][j] == 0:  # 탐색이 끝나면 바다가 된 빙산을 체크
            delList.append((i, j))
    if group > 1:  # 빙산그룹이 2개 이상이면 년을 출력
        print(year)
        break

    # 다 녹은 빙산은 탐색할 필요가 없으므로 ice에서 제거
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)