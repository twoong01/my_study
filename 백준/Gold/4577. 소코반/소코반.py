game = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    Map = [list(input()) for _ in range(n)]
    start = []
    goal = []
    for i in range(n):
        for j in range(m):
            if Map[i][j] == 'w' or Map[i][j] == 'W':
                start = [i, j]
            if Map[i][j] == '+' or Map[i][j] == 'W' or Map[i][j] == 'B':
                goal.append([i, j])
    command = list(input())
    move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    x, y = start[0], start[1]
    for com in command:
        nx = x + move[com][0]
        ny = y + move[com][1]
        if Map[nx][ny] == '.' or Map[nx][ny] == '+':
            Map[x][y] = '.'
            if [nx, ny] in goal:
                Map[nx][ny] = 'W'
            else:
                Map[nx][ny] = 'w'
            x, y = nx, ny
        elif Map[nx][ny] == 'b' or Map[nx][ny] == 'B':
            if Map[nx + move[com][0]][ny + move[com][1]] == '.':
                Map[x][y] = '.'
                if [nx, ny] in goal:
                    Map[nx][ny] = 'W'
                else:
                    Map[nx][ny] = 'w'
                if [nx + move[com][0], ny + move[com][1]] in goal:
                    Map[nx + move[com][0]][ny + move[com][1]] = 'B'
                elif Map[nx + move[com][0]][ny + move[com][1]] != '#':
                    Map[nx + move[com][0]][ny + move[com][1]] = 'b'
                x, y = nx, ny

            elif Map[nx + move[com][0]][ny + move[com][1]] == '+':
                Map[x][y] = '.'
                if [nx, ny] in goal:
                    Map[nx][ny] = 'W'
                else:
                    Map[nx][ny] = 'w'
                if [nx + move[com][0], ny + move[com][1]] in goal:
                    Map[nx + move[com][0]][ny + move[com][1]] = 'B'
                elif Map[nx + move[com][0]][ny + move[com][1]] != '#':
                    Map[nx + move[com][0]][ny + move[com][1]] = 'b'
                x, y = nx, ny
        cnt = 0
        for i in Map:
            cnt += i.count('B')
        if cnt == len(goal):
            break
    # 출력
    for i in Map:
        if '+' in i:
            print(f'Game {game}: incomplete')
            break
    else:
        print(f'Game {game}: complete')
    game += 1
    for i in range(n):
        for j in range(m):
            print(Map[i][j], end='')
        print()