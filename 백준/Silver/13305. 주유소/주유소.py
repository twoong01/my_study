N = int(input())
meter = list(map(int, input().split()))
price = list(map(int, input().split()))
ans = 0
minprice = price[0]
for i in range(N-1):
    if minprice > price[i]:
        minprice = price[i]
    ans += minprice * meter[i]

print(ans)
