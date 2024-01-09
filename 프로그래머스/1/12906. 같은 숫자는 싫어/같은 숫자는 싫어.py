def solution(arr):
    stack = []
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            top = stack[-1]
            if i != top:
                stack.append(i)
    return stack