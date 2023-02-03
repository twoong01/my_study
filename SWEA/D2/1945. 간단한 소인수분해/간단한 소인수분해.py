t = int(input())
for T in range(1, t + 1):
    n = int(input())
    ans = {2 : 0, 3 : 0, 5 : 0, 7 : 0, 11 : 0}
    while n != 1:
        if n % 11 == 0:
            n = n // 11
            ans[11] += 1
        elif n % 7 == 0:
            n = n // 7
            ans[7] += 1
        elif n % 5 == 0:
            n = n // 5
            ans[5] += 1
        elif n % 3 == 0:
            n = n // 3
            ans[3] += 1
        elif n % 2 == 0:
            n = n // 2
            ans[2] += 1
    ans = sorted(ans.items(), key=lambda x : x[0])
    lst = []
    for i in ans:
        lst.append(i[1])
    print(f'#{T} ', end='')
    print(*lst)