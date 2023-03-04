import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
m = int(input())
for _ in range(m):
    com = list(input().split())
    if com[0] == 'L':
        if left:
            right.append(left.pop())
    elif com[0] == 'D':
        if right:
            left.append(right.pop())
    elif com[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(com[1])

left.extend(reversed(right))
print(''.join(left))