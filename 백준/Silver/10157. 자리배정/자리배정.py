c, r = map(int, input().split())
k = int(input())
cnt = 1
box = [[0 for _ in range(c)] for _ in range(r)]
col = 0
row = 0
l, m = 1, -1
p, q = 0, 0
a, b = 1, 1
e, f = 1, 1
while True:
    for i in range(r - l, m, -1): # 위
        box[i][col] = cnt
        cnt += 1
    if cnt > c * r:
        break
    col += 1
    l += 1
    m += 1
    for i in range(e, c - p): # 오른쪽
        box[row][i] = cnt
        cnt += 1
    if cnt > c * r:
        break
    row += 1
    p += 1
    e += 1
    for i in range(f, r - q): # 아래
        box[i][c - a] = cnt
        cnt += 1
    if cnt > c * r:
        break
    q += 1
    a += 1
    f += 1
    for i in range(c - l, m, -1): # 왼쪽
        box[r - b][i] = cnt
        cnt += 1
    if cnt > c * r:
        break
    b += 1
for x in range(c):
    for y in range(r):
        tmp = box[y][x]
        if tmp == k:
            print(x + 1, r - y)
            exit()
else:
    print(0)
