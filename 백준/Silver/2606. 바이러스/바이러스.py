n = int(input())
k = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(v):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
            cnt += 1
cnt = 0
dfs(1)
print(cnt)