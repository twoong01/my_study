from collections import deque

n, m = map(int, input().split())
ans = []
lst = deque([i for i in range(1, n + 1)])
while lst:
    for _ in range(m - 1):
        lst.append(lst.popleft())
    ans.append(lst.popleft())
print('<', end='')
for i in range(len(ans)):
    if i != len(ans) - 1:
        print(ans[i], end=', ')
    else:
        print(ans[i], end='')
print('>')