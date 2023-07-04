def solution(s):
    answer = []
    cnt = 0
    total = 0
    while True:
        if s == '1':
            break
        tmp = ''
        for i in range(len(s)):
            if s[i] == '0':
                cnt += 1
                continue
            tmp += s[i]
        c = len(tmp)
        s = bin(c)[2:]
        total += 1
    answer.append(total)
    answer.append(cnt) 
    return answer