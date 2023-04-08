t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    maps = [[0 for _ in range(m + 2 * k)] for _ in range(n + 2 * k)]
    for i in range(n):
        lst = list(map(int, input().split()))
        for j in range(m):
            if lst[j]:
                maps[i + k][j + k] = (0, lst[j])

    for time in range(1, k + 1):
        for i in range(k - time, n + k + time):
            for j in range(k - time, m + k + time):
                if maps[i][j]:
                    nt, power = maps[i][j]
                    if 0 < time - (nt + power) <= power:
                        for l in range(4):
                            nx = i + dx[l]
                            ny = j + dy[l]
                            nw = maps[nx][ny]
                            if nw:
                                if nw[0] == time and nw[1] < power:
                                    maps[nx][ny] = (time, power)
                            else:
                                maps[nx][ny] = (time, power)
    rlt = 0
    for i in range(n + 2*k):
        for j in range(m + 2 * k):
            if maps[i][j]:
                time, power = maps[i][j]
                if k - time - power < power:
                    rlt += 1
    print(f'#{tc}', rlt)