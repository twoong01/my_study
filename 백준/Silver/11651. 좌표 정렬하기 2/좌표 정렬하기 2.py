import sys
n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
graph.sort(key=lambda x:(x[1], x[0]))

for i in graph:
    print(i[0], i[1])