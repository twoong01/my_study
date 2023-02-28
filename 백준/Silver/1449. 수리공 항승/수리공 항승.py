n, l = map(int, input().split())
m = list(map(int, input().split()))
m.sort()
start = 0
cnt = 0
for i in m:
    if start < i:
        start = i+l-1
        cnt += 1
print(cnt)
