t = int(input())
for T in range(1, t+1):
    n = int(input())
    n_lst = list(map(int, input()))
    ans = []
    cnt = 0
    for i in range(n):
        if n_lst[i] == 1:
            cnt += 1
            ans.append(cnt)
        elif n_lst[i] == 0:
            ans.append(cnt)
            cnt = 0
    print(f'#{T} {max(ans)}')
