def solution(progresses, speeds):
    answer = []
    tmp = []
    for i in range(len(progresses)):
        day = 0
        while(100 - progresses[i] > 0):
            progresses[i] += speeds[i]
            day += 1
        tmp.append(day)
    cnt = 0
    longest = 0
    for i in range(len(tmp)):
        if i == 0:
            longest = tmp[i]
            cnt += 1
        else:
            if longest >= tmp[i]:
                cnt += 1
            else:
                answer.append(cnt)
                longest = tmp[i]
                cnt = 1
    answer.append(cnt)
    return answer