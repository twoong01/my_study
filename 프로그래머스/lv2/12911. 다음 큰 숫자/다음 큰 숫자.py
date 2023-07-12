def solution(n):
    answer = 0
    small = bin(n)[2:]
    one_cnt = small.count('1')
    big = n + 1
    while True:
        tmp = bin(big)[2:].count('1')
        if tmp == one_cnt:
            break
        else:
            big += 1
    answer = big
    return answer