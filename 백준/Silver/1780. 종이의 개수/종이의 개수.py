def check(start_r, start_c, n):
    global minus_cnt, zero_cnt, one_cnt

    flag = 1
    num = n_lst[start_r][start_c]

    for i in range(start_r, start_r + n):
        for j in range(start_c, start_c + n):
            if num != n_lst[i][j]:
                flag = 0
                break

    # base condition
    if flag:
        if num == -1:
            minus_cnt += 1
        elif num == 0:
            zero_cnt += 1
        else:
            one_cnt += 1
    else:
        n //= 3
        check(start_r, start_c, n)
        check(start_r + n, start_c, n)
        check(start_r + 2 * n, start_c, n)
        check(start_r, start_c + n, n)
        check(start_r + n, start_c + n, n)
        check(start_r + 2 * n, start_c + n, n)
        check(start_r, start_c + 2 * n, n)
        check(start_r + n, start_c + 2 * n, n)
        check(start_r + 2 * n, start_c + 2 * n, n)

n = int(input())
n_lst = []
for i in range(n):
    n_lst.append(list(map(int, input().split())))

minus_cnt, zero_cnt, one_cnt = 0, 0, 0
check(0, 0, n)
print(minus_cnt)
print(zero_cnt)
print(one_cnt)