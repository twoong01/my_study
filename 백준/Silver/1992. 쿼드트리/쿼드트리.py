def quad_tree(start_r, start_c, n):
    global ans
    state = 1
    color = n_lst[start_r][start_c]

    for i in range(start_r, start_r + n):
        for j in range(start_c, start_c + n):
            if color != n_lst[i][j]:
                state = 0
                break
    if state:
        if color == 0:
            ans += '0'
        else:
            ans += '1'
    else:
        n //= 2
        ans += '('
        quad_tree(start_r, start_c, n)    # 왼쪽 위
        quad_tree(start_r, start_c + n, n) # 오른 쪽 위
        quad_tree(start_r + n, start_c, n) # 왼쪽 아래
        quad_tree(start_r + n, start_c + n, n) # 오른쪽 아래
        ans += ')'

n = int(input())
n_lst = [list(map(int, input())) for _ in range(n)]
ans = ''
quad_tree(0, 0, n)
print(ans)