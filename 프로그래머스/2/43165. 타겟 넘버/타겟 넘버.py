from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([(-1) * numbers[0], 0])
    while q:
        c_sum, c_idx = q.popleft()
        if c_idx == len(numbers) - 1:
            if c_sum == target:
                answer += 1
        else:
            if c_idx < len(numbers) - 1:
                q.append([c_sum + numbers[c_idx + 1], c_idx + 1])
                q.append([c_sum - numbers[c_idx + 1], c_idx + 1])
    return answer