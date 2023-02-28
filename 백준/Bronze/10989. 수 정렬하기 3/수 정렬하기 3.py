import sys
n = int(sys.stdin.readline())

b = [0] * 10001

for i in range(n):
    a = int(sys.stdin.readline())
    b[a] = b[a] + 1

for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)