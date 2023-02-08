import sys
input = sys.stdin.readline

n = int(input())
ans = []
for i in range(n):
    order = list(map(str, input().split()))
    if order[0] == 'push':
        ans.append(order[1])
    elif order[0] == 'pop':
        try:
            tmp = ans.pop()
            print(tmp)
        except:
            print(-1)
    elif order[0] == 'top':
        if len(ans) != 0:
            tmp = ans[-1]
            print(tmp)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(ans))
    else:
        if len(ans) == 0:
            print(1)
        else:
            print(0)