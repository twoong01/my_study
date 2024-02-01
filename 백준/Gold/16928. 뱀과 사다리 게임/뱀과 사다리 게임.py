from collections import deque

n, m = map(int, input().split())
board = [0 for _ in range(101)]
visit = [False for _ in range(101)]

for i in range(n):
    x, y = map(int, input().split())
    board[x] = [y, 'L']

for i in range(m):
    x, y = map(int, input().split())
    board[x] = [y, 'S']

q = deque()
q.append([1, 0])
visit[1] = True

while q:
    node, cnt = q.popleft()

    if node == 100:
        print(cnt)
        break

    for k in range(1, 7):
        nx = node + k
        if nx > 100: continue
        if visit[nx]: continue
        if board[nx] != 0:
            arrive, method = board[nx]
            q.append([arrive, cnt + 1])
            visit[arrive] = True
        else:
            q.append([nx, cnt + 1])
            visit[nx] = True    