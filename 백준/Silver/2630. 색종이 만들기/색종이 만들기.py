def check(start_r, start_c, n):
    global white_cnt, blue_cnt

    state = 1
    color = n_lst[start_r][start_c]

    for i in range(start_r, start_r + n):
        for j in range(start_c, start_c + n):
            if color != n_lst[i][j]:
                state = 0
                break
        if not state:
            break

    if state:
        if color == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
    else:
        n //= 2
        check(start_r, start_c, n)
        check(start_r + n, start_c, n)
        check(start_r, start_c + n, n)
        check(start_r + n, start_c + n, n)

n = int(input())
n_lst = [list(map(int, input().split())) for _ in range(n)]
white_cnt, blue_cnt = 0, 0
check(0, 0, n)
print(white_cnt)
print(blue_cnt)