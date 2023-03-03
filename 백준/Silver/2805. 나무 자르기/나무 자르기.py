n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start = 0
end = trees[-1]
ans = 0
while start <= end:
    mid = (start + end) // 2
    _sum = 0
    for tree in trees:
        if tree - mid < 0: continue
        _sum += tree - mid
    if _sum >= m:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)