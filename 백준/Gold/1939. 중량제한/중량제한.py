from collections import deque

def bfs(mid):
    isvisited[start] = True
    q = deque()
    q.append(start)
    
    while q:
        node = q.popleft()
        if node == end:
            return True
        for nx, nc in links[node]:
            if not isvisited[nx] and mid <= nc:
                q.append(nx)
                isvisited[nx] = True
    return False

n, m = map(int, input().split())
links = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    links[a].append((b, c))
    links[b].append((a, c))
for i in range(1, n + 1):
    links[i].sort(reverse=True)
start, end = map(int, input().split())

low, high = 1, 1000000000
while low <= high:
    mid = (low + high) // 2
    isvisited = [False for _ in range(n + 1)]
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1
print(high)