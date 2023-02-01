import math
t = int(input())
for T in range(t):
    A, B = map(int, input().split())
    a = A // math.gcd(A, B)
    b = B // math.gcd(A, B)
    if math.gcd(A, B) == 1:
        print(A * B)
    else:
        print(a * b * math.gcd(A, B))