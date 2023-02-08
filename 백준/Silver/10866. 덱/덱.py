import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ans = deque()
for i in range(n):
    order = list(map(str, input().split()))
    if order[0] == 'push_front':
        ans.appendleft(order[1])
    elif order[0] == 'push_back':
        ans.append(order[1])
    elif order[0] == 'pop_front':
        if len(ans) != 0:
            tmp = ans.popleft()
            print(tmp)
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if len(ans) != 0:
            tmp = ans.pop()
            print(tmp)
        else:
            print(-1)
    elif order[0] == 'empty':
        if len(ans) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'size':
        print(len(ans))
    elif order[0] == 'front':
        if len(ans) != 0:
            print(ans[0])
        else:
            print(-1)
    else:
        if len(ans) != 0:
            print(ans[-1])
        else:
            print(-1)