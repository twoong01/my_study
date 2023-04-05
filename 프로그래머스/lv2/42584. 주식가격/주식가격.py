def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        time = 0
        for j in range(i, len(prices) - 1):
            if prices[i] <= prices[j]:
                time += 1
            else:
                break
        answer.append(time)
    answer.append(0)
    return answer