def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            peek = stack[-1]
            if i == '(':
                if i == peek:
                    stack.append(i)
                else:
                    return False
            else:
                if i != peek:
                    stack.pop()
                else:
                    return False
    if stack:
        return False
    return True