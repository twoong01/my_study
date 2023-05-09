maps = [list(map(int, input().split())) for _ in range(10)]
remain = [5, 5, 5, 5, 5]
total = 25

def check(x, y, offset):
    for i in range(y, y+ offset + 1):
        for j in range(x, x + offset + 1):
            if maps[i][j] != 1: return False
    return True

def backtrack(x, y, cnt):
    global remain, total
    
    if y >= 10:
        total = min(total, cnt)
        return
    
    if x >= 10:
        backtrack(0, y + 1, cnt)
        return
    
    if maps[y][x] == 1:
        for k in range(5):
            if remain[k] == 0: continue
            if y + k >= 10 or x + k >= 10: continue

            if not check(x, y, k): break
            for i in range(y, y + k + 1):
                for j in range(x, x + k + 1):
                    maps[i][j] = 0
            remain[k] -= 1
            backtrack(x + k + 1, y, cnt + 1)
            # 원상복구
            remain[k] += 1
            for i in range(y, y + k + 1):
                for j in range(x, x + k + 1):
                    maps[i][j] = 1
    else:
        backtrack(x + 1, y, cnt)

backtrack(0, 0, 0)
print(-1 if total == 25 else total)