from collections import deque

n, m = map(int, input().split())
paper = []
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
visited = [[False for _ in range(m)] for _ in range(n)]
ans = []
for i in range(n):
    paper.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        cnt = 0
        if paper[i][j] == 1 and visited[i][j] == False:
            q = deque()
            q.append([i, j])
            visited[i][j] = True
            while q:
                cnt += 1
                x, y = q.popleft()
                for k in range(4):
                    ni = x + di[k]
                    nj = y + dj[k]
                    if 0 <= ni < n and 0 <= nj < m:
                        if paper[ni][nj] == 1 and visited[ni][nj] == False:
                            visited[ni][nj] = True
                            q.append([ni, nj])
            ans.append(cnt)
if len(ans) == 0:
    print(0)
    print(0)
else:
    print(len(ans))
    print(max(ans))
