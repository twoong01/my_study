def solution(x):
    answer = True
    total = 0
    for i in str(x):
        total += int(i)
    if x % total:
        answer = False
    return answer