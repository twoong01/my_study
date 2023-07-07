def solution(stones, k):
    answer = 0
    start, end = 1, max(stones)
    while start <= end:
        middle = (start + end) // 2
        count = 0
        max_count = 0
        flag = False
        for stone in stones:
            if stone <= middle:
                if flag:
                    count += 1
                else:
                    max_count = max(max_count, count)
                    count = 1
                    flag = True
            else:
                flag = False
        max_count = max(max_count, count)
        if max_count >= k:
            end = middle - 1
            answer = middle
        else:
            start = middle + 1
    return answer