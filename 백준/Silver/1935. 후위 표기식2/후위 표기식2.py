n = int(input())
n_lst = list(input())
num = []
for i in range(n):
    num.append(int(input()))
mat = dict()
for i in range(n):
    mat.setdefault(chr(65 + i), num[i])
stack = []
for i in n_lst:
    if i in ['+', '-', '*', '/']:
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        else:
            stack.append(a / b)
    else:
        stack.append(mat[i])
ans = stack.pop()
print('%0.2f' %(ans))