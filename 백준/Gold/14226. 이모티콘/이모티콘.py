import sys
from collections import deque

input = sys.stdin.readline

s = int(input())
emoji = [[-1 for _ in range(s + 1)] for _ in range(s + 1)]

q = deque()
q.append((1, 0))
emoji[1][0] = 0

while q:
    now, clip = q.popleft()

    if emoji[now][now] == -1:
        emoji[now][now] = emoji[now][clip] + 1
        q.append((now, now))
    
    if now + clip <= s and emoji[now + clip][clip] == -1 and clip != 0:
        q.append((now + clip, clip))
        emoji[now + clip][clip] = emoji[now][clip] + 1
    
    if now - 1 >= 0 and emoji[now - 1][clip] == -1:
        emoji[now - 1][clip] = emoji[now][clip] + 1
        q.append((now - 1, clip))

ans = -1
for i in range(s + 1):
    if emoji[s][i] != -1:
        if ans == -1 or ans > emoji[s][i]:
            ans = emoji[s][i]
print(ans)