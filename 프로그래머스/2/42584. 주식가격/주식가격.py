def solution(prices):
    answer = []
    result = []
    for i in range(len(prices)):
        tmp = prices[i]
        cnt = 0
        for j in range(i, len(prices) - 1):
            if tmp <= prices[j]:
                cnt += 1
            else:
                break
        result.append(cnt)
    answer = result
    return answer