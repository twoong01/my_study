from collections import deque

def D(n):
    return n * 2 % 10000

def S(n):
    return (n - 1) % 10000

def L(n):
    return n // 1000 + (n % 1000) * 10

def R(n):
    return n // 10 + (n % 10) * 1000


t = int(input())

methods = {'D': D, 'S': S, 'L': L, 'R': R}

for test in range(t):
    a, b = map(int, input().split())
    visited = [False for _ in range(10001)]
    q = deque()
    q.append([a, []])
    visited[a] = True
    while q:
        now, now_p = q.popleft()
        if now == b:
            print(''.join(now_p))
            break

        for name, method in methods.items():
            nx = method(now)
            if not visited[nx]:
                visited[nx] = True
                q.append([nx, now_p + [name]])