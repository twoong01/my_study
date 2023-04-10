from collections import deque
n, k = map(int, input().split())

visited = [[1e9] * 500001 for _ in range(2)]
next_to = [-1] * 500001

q = deque()
q.append([n, 0])
visited[0][n] = 0
while q:
    x, time = q.popleft()
    for i in [x - 1, 2 * x , x + 1]:
        if not(0 <= i <= 500000): continue
        if visited[(time + 1) % 2 ][i] <= time + 1: continue
        q.append([i, time + 1])
        visited[(time + 1) % 2][i] = time + 1
next_to[k] = 0
step = 1
now = k
while now < 500001:
    if visited[next_to[now] % 2][now] <= next_to[now]:
        print(next_to[now])
        break
    
    nxt = now + step
    if nxt < 500001:
        next_to[nxt] = next_to[now] + 1
    step += 1
    now = nxt
else:
    print(-1)