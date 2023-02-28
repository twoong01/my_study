import sys
input = sys.stdin.readline
k, n = map(int, input().split())
graph = []
for i in range(k):
    graph.append(int(input()))

start = 1
end = max(graph)

while start <= end:
    mid  = (start + end) // 2
    total = 0
    for i in graph:
        total += i // mid

    if total >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
