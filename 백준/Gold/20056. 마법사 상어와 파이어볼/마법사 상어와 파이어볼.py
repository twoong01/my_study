n, m, k = map(int, input().split())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
# r, c, m, s, d
fire_balls = [list(map(int, input().split())) for _ in range(m)]
maps = [[[] for _ in range(n)]for _ in range(n)]

for _ in range(k):
    while fire_balls:
        cr, cc, cm, cs, cd = fire_balls.pop(0)
        nr = (cr + cs * dx[cd]) % n
        nc = (cc + cs * dy[cd]) % n
        maps[nr][nc].append([cm, cs, cd])

    for r in range(n):
        for c in range(n):
            if len(maps[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(maps[r][c])
                while maps[r][c]:
                    _m, _s, _d = maps[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m//5:
                    for d in nd:
                        fire_balls.append([r, c, sum_m//5, sum_s//cnt, d])
            if len(maps[r][c]) == 1:
                fire_balls.append([r, c] + maps[r][c].pop())
print(sum(f[2] for f in fire_balls))
