def solution(k, tangerine):
    answer = 1
    tangerine.sort()
    
    cnt = 1
    tmp = []
    for i in range(len(tangerine)):
        if i == len(tangerine) - 1:
            tmp.append((tangerine[i], cnt))
        elif tangerine[i] == tangerine[i + 1]:
            cnt += 1
        else:
            tmp.append((tangerine[i], cnt))
            cnt = 1
    tmp = sorted(tmp, key=lambda x : x[1], reverse= True)
    total = 0
    var = 0
    for i in tmp:
        total += i[1]
        var += 1
        if total >= k:
            break
    answer = var
    return answer