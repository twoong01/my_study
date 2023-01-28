n = int(input())
for i in range(1, n+1):
    hap = i
    tmp = i
    while tmp > 0:
        hap += tmp % 10
        tmp = tmp // 10
    if hap == n:
        print(i)
        break
else:
    print(0)
