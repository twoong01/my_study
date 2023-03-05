n = int(input())
n_lst = list(input())
ans = -1e9
def operate(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper == '*':
        return num1 * num2
    else:
        return num1 - num2

def dfs(index, value):
    global ans

    if index == n - 1:
        ans = max(ans, value)
        return

    if index + 2 < n:
        dfs(index + 2, operate(value, n_lst[index + 1], int(n_lst[index + 2])))

    if index + 4 < n:
        dfs(index + 4, operate(value, n_lst[index + 1], operate(int(n_lst[index + 2]), n_lst[index +3], int(n_lst[index + 4]))))

dfs(0, int(n_lst[0]))
print(ans)