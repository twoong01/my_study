t = int(input())
for T in range(1, t + 1):
    total, A, B, fly = map(int, input().split())
    t = total/(A+B)
    ans = fly * t
    print(f'#{T} {ans}')