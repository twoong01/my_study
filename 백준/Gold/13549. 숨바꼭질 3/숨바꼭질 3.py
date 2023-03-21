from collections import deque
n, k = map(int, input().split())
isvisited = [False] * 100001

q = deque()
q.append((n, 0))
isvisited[n] = True
while q:
    x, time = q.popleft()
    if x == k:
        print(time)
        break
    for nx in [x * 2, x - 1, x + 1]:
        if not(0 <= nx <= 100000): continue
        if isvisited[nx]: continue
        isvisited[nx] = True
        if nx == x * 2:
            q.append((nx, time))
        else:
            q.append((nx, time + 1))