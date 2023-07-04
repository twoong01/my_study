def solution(s):
    answer = ''
    tmp_s = s.split(' ')
    tmp = []
    for i in tmp_s:
        tmp.append(int(i))
    answer += str(min(tmp)) + ' '
    answer += str(max(tmp))
    return answer