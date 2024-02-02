import sys
input = sys.stdin.readline

n, m = map(int, input().split())
link = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a not in link:
        link.setdefault(a, [b])
    else:
        link[a] += [b]
    
    if b not in link:
        link.setdefault(b, [a])
    else:
        link[b] += [a]

from collections import deque
ans = []
for i in range(1, n + 1):
    q = deque()
    q.append([i, 0])
    visited = [False for _ in range(n)]
    visited[i - 1] = True
    kbnum = 0
    while q:
        node, cnt = q.popleft()
        
        if node in link:
            for j in link[node]:
                if visited[j - 1]:
                    pass
                else:
                    q.append([j, cnt + 1])
                    visited[j - 1] = True
                    kbnum += cnt + 1
    ans.append(kbnum)
print(ans.index(min(ans)) + 1)