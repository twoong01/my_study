total = int(input())
k = int(input())
hap = 0
for i in range(k):
    n, m = map(int, input().split())
    hap += n*m

if hap == total:
    print('Yes')
else:
    print('No')