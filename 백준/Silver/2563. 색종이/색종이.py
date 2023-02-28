import collections
t = int(input())
box = [[0] * 101 for _ in range(101)]

for _ in range(t):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            box[x + i][y + j] += 1
cnt = 0
for i in range(101):
    for j in range(101):
        if box[i][j] >= 1:
            cnt += 1
print(cnt)
