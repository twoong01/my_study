box = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = (list(map(int, input().split())))
    for x in range(x1, x2):
        for y in range(y1, y2):
            box[x][y] = 1 
ans = 0
for i in range(100):
    for j in range(100):
        if box[i][j] == 1:
            ans += 1
print(ans)