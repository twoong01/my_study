n, s = map(int, input().split())
n_lst = list(map(int, input().split()))
cnt = 0
for i in range(1, 1 << len(n_lst)):
    hap  = []
    for j in range(len(n_lst)):
        if i & (1 << j):
            hap.append(n_lst[j])
    if sum(hap) == s:
        cnt += 1
print(cnt)