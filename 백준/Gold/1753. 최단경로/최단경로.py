import heapq, sys

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        w, node = heapq.heappop(q)
        if dp[node] < w:
            continue

        for nw, nx in graph[node]:
            d = w + nw
            if d < dp[nx]:
                dp[nx] = d
                heapq.heappush(q, [d, nx])


V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]
INF = sys.maxsize
dp = [INF] * (V + 1)
q = []



for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
dijkstra(k)
for i in range(1, V + 1):
    print("INF" if dp[i] == INF else dp[i])