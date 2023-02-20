from collections import deque

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
q = deque([0] * w)
time = 0
while q:
    time += 1
    q.popleft()

    if trucks:
        if sum(q) + trucks[0] > l:
            q.append(0)
        else:
            q.append(trucks.pop(0))
print(time)