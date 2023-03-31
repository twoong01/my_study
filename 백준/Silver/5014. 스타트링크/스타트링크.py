from collections import deque
F, S, G, U, D = map(int, input().split())
dy = [U, -D]


q = deque()
q.append((S, 0))
visited = [False] * (F + 1)
visited[S] = True
while q:
    s, cnt = q.popleft()
    if s == G:
        print(cnt)
        break
    for k in range(2):
        ns = s + dy[k]
        if not(0 < ns <= F): continue
        if visited[ns]: continue
        visited[ns] = True
        q.append((ns, cnt + 1))
else:
    print('use the stairs')