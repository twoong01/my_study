n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.reverse()
cnt = 0
for i in range(0, n):
    if(a[i] <= k):
        cnt += k//a[i]
        k = k%a[i]
    else:
        continue
print(cnt)