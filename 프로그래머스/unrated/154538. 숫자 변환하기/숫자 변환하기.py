from collections import deque
def solution(x, y, n):
    answer = 0
    
    isvisited = [False for _ in range(y + 1)]
    q = deque()
    q.append(x)
    isvisited[x] = 0
    while q:
        now = q.popleft()
        if now == y:
            answer = isvisited[now]
            return answer
        for d in [3*now, 2*now, n+now]:
            if not(1 <= d <= y): continue
            if isvisited[d]: continue
            q.append(d)
            isvisited[d] = isvisited[now] + 1
    
    
    return -1