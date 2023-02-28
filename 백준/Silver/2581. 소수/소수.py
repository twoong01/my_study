m = int(input())
n = int(input())
prime = set()
for i in range(m, n+1):
    if i == 1:
        pass
    else:
        for j in range(2, i+1):
            if i % j == 0 and i != j:
                break
        else:
            prime.add(i)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))
