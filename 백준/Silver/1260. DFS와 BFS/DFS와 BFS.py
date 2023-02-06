n, m, v = map(int, input().split())
graph = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    elif b not in graph[a]:
        graph[a].append(b)
    if b not in graph:
        graph[b] = [a]
    if a not in graph[b]:
        graph[b].append(a)

def dfs(graph, start):
    need_visited, visited = list(), list()
    need_visited.append(start)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = graph[node]
                temp.sort(reverse=True)
                need_visited.extend(temp)
    return visited

def bfs(graph, start):
    need_visited, visited = list([start]), list()
    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = graph[node]
                temp.sort()
                need_visited += temp
    return visited

print(*dfs(graph, v))
print(*bfs(graph, v))