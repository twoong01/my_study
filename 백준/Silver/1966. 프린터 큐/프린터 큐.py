from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    m += 1
    idx_lst = deque([j for j in range(1, n + 1)])
    doc = deque(list(map(int, input().split())))
    cnt = 0
    while doc:
        mx = max(doc)
        now = doc.popleft()
        idx_now = idx_lst.popleft()
        if now < mx:
            doc.append(now)
            idx_lst.append(idx_now)
        else:
            if idx_now == m:
                break
            cnt += 1
    print(cnt + 1)