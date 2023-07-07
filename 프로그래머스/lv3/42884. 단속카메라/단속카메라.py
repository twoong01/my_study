def solution(routes):
    routes.sort(key = lambda x: x[0])
    answer = 1
    middle = 30000
    for i, j in routes:
        if i > middle:
            middle = j
            answer += 1
        middle = min(middle, j)
        print(middle)
    return answer