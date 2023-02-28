n = int(input())
ans = []
if n == 1:
    pass
else:
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                ans.append(i)
                n = n // i
                break
for i in ans:
    print(i)