def solution(order):
    answer = 0
    stack = []
    total = len(order)
    idx = 0
    for num in range(1, total + 1):
        stack.append(num)
        
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
            answer += 1
    return answer