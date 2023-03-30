n = int(input())
lst = [int(input()) for _ in range(n)]

dp = [0] * n

dp[0] = lst[0]
if n > 1:
    dp[1] = lst[1] + lst[0]
if n > 2:
    dp[2] = max(lst[1] + lst[2], lst[2] + lst[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i - 3] + lst[i] + lst[i - 1], dp[i - 2] + lst[i], dp[i - 1])
print(dp[n - 1])