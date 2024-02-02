def is_min(mini):
    left = 0
    cnt = 0
    for right in cut:
        if right - left >= mini:
            left = right
            cnt += 1
    if cnt > k:
        return True
    return False

n, m, l = map(int, input().split())
cut = []
for i in range(m):
    cut.append(int(input()))
cut += [l]

for j in range(n):
    k = int(input())
    start = 1
    end = 4000000
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if is_min(mid):
            start = mid + 1
            ans = max(mid, ans)
        else:
            end = mid - 1
    print(ans)