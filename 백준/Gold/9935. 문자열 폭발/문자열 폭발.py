n_lst = input()
bomb = list(input())
bomb_last = bomb[-1]
stack = []
for i in n_lst:
    stack.append(i)
    if stack[-1] == bomb_last and bomb == stack[-len(bomb):]:
        del stack[-len(bomb):]
if len(stack) != 0:
    for i in stack:
        result = ''.join(i)
        print(result, end='')
else:
    print('FRULA')