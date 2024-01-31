def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append (arr[i])
        else:
            top = answer[-1]
            if top != arr[i]:
                answer.append(arr[i])
    return answer