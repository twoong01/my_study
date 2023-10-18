def solution(progresses, speeds):
    answer = []
    tmp = []
    for i in range(len(progresses)):
        upload = 0
        days = 0
        while (100 - progresses[i]) > upload:
            upload += speeds[i]
            days += 1
        tmp.append(days)
    print(tmp)
    cnt = 0
    longest = 0
    for i in range(len(tmp)):
        if i == 0:
            cnt += 1
            longest = tmp[i]
        else:
            if longest >= tmp[i]:
                cnt += 1
            else:
                answer.append(cnt)
                longest = tmp[i]
                cnt = 1
    answer.append(cnt)
    return answer