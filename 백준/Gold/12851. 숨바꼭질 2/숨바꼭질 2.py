from collections import deque
n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]

q = deque()
q.append(n)
visited[n][0] = 0
visited[n][1] = 1
while q:
    x = q.popleft()
    for nx in [x - 1, 2 * x, x + 1]:
        if not(0 <= nx < 100001): continue
        if visited[nx][0] == -1:
            q.append(nx)
            visited[nx][0] = visited[x][0] + 1
            visited[nx][1] = visited[x][1]
        elif visited[nx][0] == visited[x][0] + 1:
            visited[nx][1] += visited[x][1]
print(visited[k][0])
print(visited[k][1])