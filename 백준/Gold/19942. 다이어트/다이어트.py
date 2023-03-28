n = int(input())
least = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(n)]
ans = 1e9
ans_idx = []

for i in range(0, (1<<n)):
    tmp = []
    cnt = 0
    mine = [0, 0, 0, 0, 0]
    idx = []
    for j in range(0, n):
        if i & (1 << j):
            tmp.append(lst[j])
            idx.append(j + 1)
    for k in tmp:
        for l in range(5):
            mine[l] += k[l]
    for l in range(4):
        if mine[l] >= least[l]:
            cnt += 1
    if cnt == 4:
        if ans > mine[-1]:
            ans = mine[-1]
            ans_idx = idx

        elif ans == mine[-1]:
            if len(ans_idx) == 0:
                ans_idx = idx
            else:
                tmp_idx = [ans_idx, idx]
                tmp_idx.sort()
                ans_idx = tmp_idx[0]
if ans == 1e9:
    print(-1)
else:
    print(ans)
    print(*ans_idx)
