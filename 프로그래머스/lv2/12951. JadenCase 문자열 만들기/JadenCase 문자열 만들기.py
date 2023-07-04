def solution(s):
    answer = ''
    flag = False
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
        else:
            if s[i] == ' ':
                answer += s[i]
                flag = True
            else:
                if flag:
                    answer += s[i].upper()
                    flag = False
                else:
                    answer += s[i].lower()
    return answer