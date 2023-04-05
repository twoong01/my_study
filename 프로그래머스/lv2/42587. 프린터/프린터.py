from collections import deque
def solution(priorities, location):
    answer = 0
    target = (priorities[location], location)
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    result = []
    while q:
        now = q.popleft()
        if q:
            mx = max(q)[0]
            if now[0] < mx:
                q.append(now)
            else:
                result.append(now)
        else:
            result.append(now)      
    answer = result.index(target) + 1
    return answer