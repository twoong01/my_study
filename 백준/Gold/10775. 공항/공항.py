import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
plane = [int(input().rstrip('\n')) for _ in range(0,p)]
def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = {i: i for i in range(0, g+1)}
cnt = 0
for i in plane:
    x = find(i)
    if x == 0:
        break
    union(x, x-1)
    cnt += 1
print(cnt)