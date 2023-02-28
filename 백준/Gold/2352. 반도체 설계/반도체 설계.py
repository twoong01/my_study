import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
list = []

for i in graph:
    k = bisect_left(list, i)
    if len(list) <= k:
        list.append(i)
    else:
        list[k] = i
print(len(list))



