def solution(s):
    answer = []
    cnt = 0
    cnt_0 = 0;
    while True:
        tmp = ''
        for i in s:
            if i == '0':
                cnt_0 += 1
            else:
                tmp += i
        length = len(tmp)
        cnt += 1
        s = bin(length)[2:]
        if length == 1:
            break;
    answer.append(cnt)
    answer.append(cnt_0)
    return answer