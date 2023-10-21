def solution(land):
    answer = 0
    n = len(land)
    for i in range(1, n):
        for j in range(4):
            tmp = land[i - 1][j]
            land[i - 1][j] = -1
            land[i][j] += max(land[i - 1])
            land[i - 1][j] = tmp
        answer = max(land[i])
    return answer