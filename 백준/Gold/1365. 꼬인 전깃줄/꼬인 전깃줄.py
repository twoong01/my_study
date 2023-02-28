import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
lines = list(map(int, input().split()))
cut = []

for i in lines:
    k = bisect_left(cut, i)
    if len(cut) <= k:
        cut.append(i)
    else:
        cut[k] = i
print(len(lines) - len(cut))
