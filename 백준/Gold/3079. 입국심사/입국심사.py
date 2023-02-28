import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(int(input()))
answer = 0
start = 1
end = max(graph) * m
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in graph:
        total += mid // i
        if total >= m:
            break
    if total >= m:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)
