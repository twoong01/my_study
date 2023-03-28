n, r, l, x = map(int, input().split())
hard = list(map(int, input().split()))
ans = 0

for i in range(0, (1<<n)):
    tmp = []
    for j in range(0, n):
        if i & (1 << j):
            tmp.append(hard[j])
    tmp = sorted(tmp)
    if r <= sum(tmp) <= l:
        if tmp[-1] - tmp[0] >= x:
            ans += 1
print(ans)
