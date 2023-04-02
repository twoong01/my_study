def solution(name, yearning, photo):
    answer = []
    for i in photo:
        tmp = 0
        for idx, value in enumerate(name):
            if value in i:
                tmp += yearning[idx]
        answer.append(tmp)
    return answer