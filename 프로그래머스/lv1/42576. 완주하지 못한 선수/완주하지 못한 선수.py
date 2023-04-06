def solution(participant, completion):
    answer = ''
    
    p1 = dict()
    for i in participant:
        if i not in p1:
            p1.setdefault(i, 1)
        else:
            p1[i] += 1
    p2 = dict()
    for i in completion:
        if i not in p2:
            p2.setdefault(i, 1)
        else:
            p2[i] += 1
    for key, value in p1.items():
        if key not in p2 or p2[key] != value:
            answer = key
    return answer