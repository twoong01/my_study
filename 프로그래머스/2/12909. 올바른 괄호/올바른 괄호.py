from collections import deque
def solution(s):
    answer = True
    q = deque(s)
    cnt1 = 0
    cnt2 = 0
    while q:
        n = q.popleft()
        if n == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        
        if cnt1 == cnt2:
            cnt1 = 0
            cnt2 = 0
        if cnt2 > cnt1:
            return False
    if cnt1 != cnt2:
        return False
    return True