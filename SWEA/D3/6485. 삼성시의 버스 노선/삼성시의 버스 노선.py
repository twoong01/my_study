t = int(input())
for T in range(1, t + 1):
    n = int(input())
    A_bus, B_bus = [], []
    for i in range(n):
        A, B = map(int, input().split())
        A_bus.append(A)
        B_bus.append(B)
    P = int(input())
    C_stop = []
    for i in range(P):
        C = int(input())
        C_stop.append(C)
    ans = []
    for i in C_stop:
        cnt = 0
        for j in range(n):
            if i in range(A_bus[j], B_bus[j] + 1):
                cnt += 1
        ans.append(cnt)
    print(f'#{T}', end=' ')
    print(*ans)