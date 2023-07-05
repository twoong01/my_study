def solution(operations):
    answer = []
    tmp = []
    for i in operations:
        oper, num = i.split(' ')
        if oper == 'I':
            tmp.append(int(num))
        else:
            if len(tmp) == 0: continue
            if num == '-1':
                tmp.pop(tmp.index(min(tmp)))
            else:
                tmp.pop(tmp.index(max(tmp)))
    if len(tmp) == 0:
        answer =[0, 0]
    else:
        answer.append(max(tmp))
        answer.append(min(tmp))
    return answer