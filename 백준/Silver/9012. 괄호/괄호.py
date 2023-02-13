def check(n_lst):
    global stack
    for ch in n_lst:
        if len(stack) == 0:
            stack.append(ch)
        else:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if stack.pop() == '(':
                    continue
                return False
    if not stack:
        return True
    return False


t = int(input())
for tc in range(t):
    stack = []
    n_lst = list(input())
    if check(n_lst):
        print('YES')
    else:
        print('NO')