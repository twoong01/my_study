import sys
input = sys.stdin.readline
n, c = map(int, input().split())
graph = []
for i in range(n):
    graph.append(int(input()))
graph.sort()

start = 0
end = graph[-1] - graph[0]
def binary(graph, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = graph[0]
        count = 1
        for i in range(1, len(graph)):
            if graph[i] >= current + mid:
                count += 1
                current = graph[i]
        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

binary(graph, start, end)
print(answer)