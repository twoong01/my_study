import sys
input = sys.stdin.readline
n = int(input())
ans = []
for i in range(n):
    order = list(map(str, input().split()))
    if order[0] == 'push':
        ans.append(order[1])
    elif order[0] == 'pop':
        if len(ans) == 0:
            print(-1)
        else:
            tmp = ans[0]
            ans.remove(tmp)
            print(tmp)
    elif order[0] == 'size':
        print(len(ans))
    elif order[0] == 'front':
        if len(ans) == 0:
            print(-1)
        else:
            tmp = ans[0]
            print(tmp)
    elif order[0] == 'back':
        if len(ans) == 0:
            print(-1)
        else:
            tmp = ans[-1]
            print(tmp)
    else:
        if len(ans) == 0:
            print(1)
        else:
            print(0)

