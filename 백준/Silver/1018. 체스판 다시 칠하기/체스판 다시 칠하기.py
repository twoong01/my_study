n, m = map(int, input().split())
board = list()
ans = list()
for i in range(n):
    board.append(input())
for i in range(n-7):
    for j in range(m-7):
        draw_1 = 0
        draw_2 = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'B':
                        draw_1 += 1
                    if board[x][y] != 'W':
                        draw_2 += 1
                else:
                    if board[x][y] != 'W':
                        draw_1 += 1
                    if board[x][y] != 'B':
                        draw_2 += 1
        ans.append(draw_2)
        ans.append(draw_1)
print(min(ans))