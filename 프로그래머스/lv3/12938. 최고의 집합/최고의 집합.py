def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    for _ in range(n):
        answer.append(s // n)
    index = len(answer) - 1
    for i in range(s - sum(answer)):
        answer[index] += 1
        index -= 1
    return answer