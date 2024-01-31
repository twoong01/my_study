from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    target = [priorities[location], location]
    result = []
    for i in range(len(priorities)):
        q.append([priorities[i], i])
    while q:
        pri, idx = q.popleft()
        if q:
            first = max(q)[0]
            if pri < first:
                q.append([pri, idx])
            else:
                result.append([pri, idx])
        else:
            result.append([pri, idx])
    answer = result.index(target) + 1
    return answer