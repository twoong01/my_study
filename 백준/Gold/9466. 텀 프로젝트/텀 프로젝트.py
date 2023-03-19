import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)



def dfs(i):
    global result
    visited[i] = True
    cycle.append(i)
    node = graph[i]

    if visited[node]:
        if node in cycle:
            result += cycle[cycle.index(node):]
        return
    else:
        dfs(node)


t = int(input())
for _ in range(t):
    n = int(input())
    graph = dict()
    n_lst = list(map(int, input().split()))
    for idx, value in enumerate(n_lst):
        graph.setdefault(idx + 1, value)
    visited = [True] + [False] * n
    result = []
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - len(result))