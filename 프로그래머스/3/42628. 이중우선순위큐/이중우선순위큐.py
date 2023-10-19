def solution(operations):
    answer = []
    tmp = []
    for i in operations:
        operation, num = i.split(' ')
        if operation == 'I':
            tmp.append(int(num))
        else:
            if len(tmp) == 0: continue
            if num == '-1':
                tmp.pop(tmp.index(min(tmp)))              
            else:
                tmp.pop(tmp.index(max(tmp)))
    if len(tmp) == 0:
        return [0, 0]
    else:
        return [max(tmp), min(tmp)]
    return answer