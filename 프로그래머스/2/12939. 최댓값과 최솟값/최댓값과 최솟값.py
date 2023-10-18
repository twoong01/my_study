def solution(s):
    answer = ''
    numbers = list(map(int, s.split(' ')))
    mx = max(numbers)
    mn = min(numbers)
    answer = str(mn) + str(' ') + str(mx)
    return answer