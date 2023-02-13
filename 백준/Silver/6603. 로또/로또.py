def generate(m):
    if m == 6:
        if chosen == sorted(chosen):
            print(*chosen)
        return
    else:
        for i in range(k):
            if not isused[i]:
                isused[i] = True
                chosen.append(n_lst[i])
                generate(m + 1)
                isused[i] = False
                chosen.pop()

while True:
    tmp = list(map(int, input().split()))
    k = tmp[0]
    n_lst = tmp[1:]
    isused = [False] * k
    chosen = []
    if len(n_lst) == 0:
        break
    generate(0)
    print()