# 몫의 개수를 센다
import sys
input = sys.stdin.readline
t = int(input())
c = []
for _ in range(t):
    c.append(int(input()))

for i in c:
    q = d = n = p = 0
    while i != 0:
        q += i//25
        i -= 25*(q)

        d += i//10
        i -= 10*(d)

        n += i//5
        i -= 5*n

        p += i//1
        i -= 1*p
    print(q,d,n,p)