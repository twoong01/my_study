import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
graph.sort()
m = int(input())
start = 0
end = max(graph)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in graph:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= m: # 지출 양이 예산보다 작으면
        start = mid + 1
    else: # 지출 양이 예산보다 크면
        end = mid - 1

print(end)