from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    
    move = {'d' : (1, 0), 'l' : (0, -1), 'u' : (-1, 0), 'r' : (0, 1)}
    q = deque()
    q.append((x, y, '', 0))
    while q:
        now_x , now_y, history, cnt = q.popleft()
        if (now_x, now_y) == (r, c) and cnt == k:
            answer = history
            return answer
        for j in ['d', 'l', 'r', 'u']:
            nx = now_x + move[j][0]
            ny = now_y + move[j][1]
            if not(1 <= nx <= n and 1 <= ny <= m): continue
            if abs(nx - r) + abs(ny - c) + cnt + 1 > k:continue
            q.append((nx, ny, history + j, cnt + 1))
            break
    
    return 'impossible'