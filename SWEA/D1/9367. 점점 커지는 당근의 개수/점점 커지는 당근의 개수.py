
t = int(input())
for T in range(1, t + 1):
    n = int(input())
    n_lst = list(map(int, input().split()))
    c = []
    tmp = 0
    for i in range(n - 1):
        tmp = n_lst[i + 1] - n_lst[i]
        if tmp > 0:
            if i == 0:
                continue
            else:
                c.append(n_lst[i])
            if i == n - 2:
                c.append(n_lst[i])
                c.append(n_lst[i+1])
    if len(c) == 0:
        print(f'#{T} 1')
    else:
        print(f'#{T} {max(c)}')