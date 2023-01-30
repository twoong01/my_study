n, m = map(int, input().split())
S, test = [], []
for i in range(n):
    S.append(input())
for i in range(m):
    test.append(input())
check = dict()
for i in S:
    if i in check:
        check[i] += 1
    else:
        check.setdefault(i, 1)

ans = 0
for i in test:
    if i in check:
        ans += 1
    else:
        pass
print(ans)