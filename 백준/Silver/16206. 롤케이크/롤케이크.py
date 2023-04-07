n, m = map(int, input().split())
cakes = list(map(int, input().split()))
cakes = sorted(cakes, key = lambda x : (x % 10, x))
total = 0
for cake in cakes:
    cnt = cake // 10
    if cake % 10 == 0:
        if cnt - 1 <= m:
            total += cnt
            m -= cnt - 1
        else:
            total += m
            m -= m
    else:
        if cnt <= m:
            total += cnt
            m -= cnt
        else:
            total += m
            m -= m
print(total)