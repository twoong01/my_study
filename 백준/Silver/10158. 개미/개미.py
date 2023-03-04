import sys
input = sys.stdin.readline
w, h = map(int, input().split())
x, y = map(int, input().split())
time = int(input())

Tw = time % (2*w)
Th = time % (2*h)

x = x + Tw
y = y + Th

if x > w: x = 2 * w - x
if y > h: y = 2 * h - y
if x < 0: x = -x
if y < 0: y = -y
print(x, y)