n = int(input())
consult = []
for i in range(n):
    consult.append(list(map(int, input().split())))
dp = [0 for _ in range(n + 1)]

for i in range(n - 1, -1, -1):
    t, p = consult[i][0], consult[i][1]

    if i + t <= n:
        dp[i] = max(p + dp[i + t], dp[i + 1])
    else:
        dp[i] = dp[i + 1]
print(dp[0])