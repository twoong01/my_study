from collections import Counter
n, m = map(int, input().split())
trees = Counter(map(int, input().split()))

start = 0
end = max(trees.items())[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    _sum = sum((h - mid)*i for h, i in trees.items() if h > mid)
    if _sum >= m:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)