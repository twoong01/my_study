n = int(input())
box = [[0 for _ in range(1001)] for _ in range(1001)]
for i in range(1, n + 1):
    x, y, w, h = map(int, input().split())
    for j in range(y, y + h):
        box[j][x : x+w] = [i] * w

for i in range(1, n+1):
    ans = 0
    for j in range(1001):
        ans += box[j].count(i)
    print(ans)
