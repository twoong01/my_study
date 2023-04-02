def solution(park, routes):
    answer = []
    move = {'E' : (0, 1), 'W' : (0, -1), 'N' : (-1, 0), 'S' : (1, 0)}
    H = 0
    for i in park:
        W = len(i)
        if 'S' in i:
            sx = H
            sy = i.index('S')
        H += 1
    for i in routes:
        dir, cnt = i.split()
        nx, ny = sx, sy
        for _ in range(int(cnt)):
            nx += move[dir][0]
            ny += move[dir][1]
            if not(0 <= nx < H and 0 <= ny < W) or park[nx][ny] == 'X':
                nx, ny = sx, sy
                break
        sx, sy = nx, ny
    answer.append(sx)
    answer.append(sy)
    return answer