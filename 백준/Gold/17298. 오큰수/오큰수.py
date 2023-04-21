n = int(input())
n_lst = list(map(int, input().split()))
ans = [-1 for _ in range(n)]
stack = []
for i in range(n):
    while stack and n_lst[stack[-1]] < n_lst[i]:
        ans[stack.pop()] = n_lst[i]
    stack.append(i)
print(*ans)