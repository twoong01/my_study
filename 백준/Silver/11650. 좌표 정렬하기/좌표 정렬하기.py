import sys
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
graph.sort()
for i in graph:
    print(i[0], i[1])