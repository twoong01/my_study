from collections import deque
n, m = map(int, input().split())
visited = [-1] * 100001
path = []

q = deque()
q.append((n, 0))
while q:
    x, time = q.popleft()
    if x == m:
        idx = x
        print(time)
        while idx != n:
            path.append(idx)
            idx = visited[idx]
        path.append(n)
        break
    for nx in [x + 1, x - 1, 2 * x]:
        if not(0 <= nx <= 100000): continue
        if visited[nx] != -1: continue
        visited[nx] = x
        q.append((nx, time + 1))
print(*path[::-1])