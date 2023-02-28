N = int(input())
T = []
for i in range(N):
    a, b = map(int, input().split())
    T.append((a,b))
T.sort(key=lambda x:(x[1], x[0]))
start = 0
cnt = 0
for meeting in T:
    if meeting[0] >= start:
        cnt += 1
        start = meeting[1]
print(cnt)