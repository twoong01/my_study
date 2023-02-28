T = int(input())
c1 = c2 = c3 = 0
while True:
    if T % 300 == 0:
        c1 += T // 300
        print(c1, c2, c3)
        break
    elif T % 60 == 0:
        c2 += T // 60
        print(c1, c2, c3)
        break
    T -= 10
    c3 += 1
    if T < 0:
        print(-1)
        break