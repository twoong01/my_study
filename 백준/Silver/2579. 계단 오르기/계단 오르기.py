N=int(input())
arr=[int(input()) for _ in range(N)]
if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0] + arr[1])
else:
    dp=[0]*N
    dp[0]=arr[0]
    dp[1]=dp[0]+arr[1]
    dp[2]=max(arr[1]+arr[2], arr[0]+arr[2])
    for i in range(3, N):
        dp[i]=max(dp[i-3]+arr[~-i]+arr[i], dp[i-2]+arr[i])
    print(dp[N-1])