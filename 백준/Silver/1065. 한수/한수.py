n = int(input())
cnt = 0
if n < 100:
    print(n)
else:
    cnt = 99
    for i in range(100, n + 1):
        hun = i // 100
        ten = (i // 10) % 10
        one = i % 10 

        if((hun - ten) == (ten - one)):
            cnt += 1
    print(cnt)