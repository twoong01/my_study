def solution(n):
    answer = ""
    lst = []
    while n > 0:
        tmp = n % 10
        lst.append(str(tmp))
        n //= 10
    lst = sorted(lst, reverse=True)
    for i in lst:
        answer += i
    return int(answer)