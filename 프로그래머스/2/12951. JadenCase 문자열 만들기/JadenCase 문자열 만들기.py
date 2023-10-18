def solution(s):
    answer = ''
    tmp = False
    for index, word in enumerate(s):
        if index == 0:
            answer += word.upper()
            continue
            
        if word == ' ':
            tmp = True
            answer += word
        elif word != ' ':
            if tmp:
                answer += word.upper()
                tmp = False
            else:
                answer += word.lower()
                tmp = False
    return answer