n = int(input())
isvisited_s = [False] * n # 세로
isvisited_g = [False] * n # 가로
isvisited_lh = [False] * (2*n) # 대각선 
isvisited_ll = [False] * (2*n) # 대각선
cnt = 0

def N_queen(depth):
    global cnt
    if depth == n:
        cnt += 1
        return
    else:
        for i in range(n):
            if not isvisited_g[i] and not isvisited_s[i] and not isvisited_lh[i + depth] and not isvisited_ll[depth - i + n - 1]:
                isvisited_s[i] = True
                isvisited_g[i] = True
                isvisited_lh[i + depth] = True
                isvisited_ll[depth - i + n - 1] = True
                N_queen(depth + 1)
                isvisited_s[i] = False
                isvisited_g[i] = False
                isvisited_lh[i + depth] = False
                isvisited_ll[depth - i + n - 1] = False

N_queen(0)
print(cnt)