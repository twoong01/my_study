T = int(input())
for t in range(T):
    ans = ''
    n, m = input().split()
    for i in range(len(m)):
        ans += m[i]*int(n)
    print(ans)
