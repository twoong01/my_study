n_lst = list(input())
stack = [n_lst[0]]
cnt = 0
for i in range(1, len(n_lst)):
    if len(stack) == 0:
        stack.append(n_lst[i])
    else:
        if n_lst[i] == '(':
            stack.append(n_lst[i])
        else:
            if n_lst[i - 1] == '(':
                stack.pop()
                cnt += len(stack)
            else:
                cnt += 1
                stack.pop()
print(cnt)