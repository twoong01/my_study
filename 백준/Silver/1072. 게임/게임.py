from math import floor
import sys
input = sys.stdin.readline
x,y = map(int, input().split())
z = floor(100*y/x)
start = 0
end = 1000000000
if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start+end)//2
        tx, ty = x + mid, y + mid
        if floor(100*ty/tx) > z:
            end = mid - 1
        else:
            start = mid + 1
    print(end + 1)
