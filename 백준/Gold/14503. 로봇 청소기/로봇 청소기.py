n, m = map(int, input().split())
# 첫 위치 : (r, c), 청소기의 방향 : d (0 : 북, 1 : 동, 2 : 남, 3 : 서)
r, c, d = map(int, input().split())
# 0 : 청소 x, 1 : 벽
room = [list(map(int, input().split())) for _ in range(n)]
isvisited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
state = True
isvisited[r][c] = True
cnt = 1
while True:
    for i in range(4):
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4
        if 0 <= nx < n and 0 <= ny < m and not room[nx][ny]:
            if not isvisited[nx][ny]:
                isvisited[nx][ny] = True
                cnt += 1
                r = nx
                c = ny
                break
    else:   
        if room[r-dx[d]][c-dy[d]]:
            print(cnt)
            break
        else:
            r = r - dx[d]
            c = c - dy[d]