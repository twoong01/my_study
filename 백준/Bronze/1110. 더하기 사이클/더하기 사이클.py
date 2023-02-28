N = int(input())
res = 0
n = N
n_1 = N // 10
n_2 = N % 10
cnt = 0
while True:
    n_1 = n // 10
    n_2 = n % 10
    res = n_1 + n_2
    n = n_2*10 + res%10
    cnt += 1
    if n == N:
        break
print(cnt)
