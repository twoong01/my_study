from collections import deque

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))


a, b, c = map(int, input().split())

q = deque()
q.append((0, 0))
visited = [[False for _ in range(b + 1)] for _ in range(a + 1)]
visited[0][0] = True

ans = []
while q:
    x, y = q.popleft()
    z = c - x - y

    if x == 0:
        ans.append(z)

    # A에서 B로 물 이동
    water = min(x, b - y)
    pour(x - water, y + water)
    # A에서 C로 물 이동
    water = min(x, c - z)
    pour(x - water, y)

    # B에서 C로 물 이동
    water = min(x, c - z)
    pour(x - water, y)
    # B에서 A로 물 이동
    water = min(y, a - x)
    pour(x + water, y - water)

    # C에서 A로 물 이동
    water = min(z, a - x)
    pour(x + water, y)
    # C에서 B로 물 이동
    water = min(z, b - y)
    pour(x, y + water)

ans.sort()
print(*ans)
