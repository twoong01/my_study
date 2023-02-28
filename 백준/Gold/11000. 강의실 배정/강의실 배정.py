import heapq
import sys
input = sys.stdin.readline
n = int(input())
time = []
for i in range(n):
    s, t = map(int, input().split())
    time.append([s, t])
time.sort(key=lambda x:(x[0],x[1]))

cnt = []
heapq.heappush(cnt, time[0][1])
for i in range(1, n):
    if time[i][0] < cnt[0]:
        heapq.heappush(cnt, time[i][1])
    else:
        heapq.heappop(cnt)
        heapq.heappush(cnt, time[i][1])
print(len(cnt))

        
