def solution(s):
    answer = ''
    sorted_s = sorted(s, reverse=True)
    for i in sorted_s:
        answer += i
    return answer