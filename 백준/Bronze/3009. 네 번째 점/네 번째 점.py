lst = []
for i in range(3):
    lst.append(list(map(int, input().split())))
x = dict()
y = dict()
for i in range(3):
    for j in range(2):
        if j == 0:
            if lst[i][j] in x:
                x[lst[i][j]] += 1
            else:
                x.setdefault(lst[i][j], 1)
        else:
            if lst[i][j] in y:
                y[lst[i][j]] += 1
            else:
                y.setdefault(lst[i][j], 1)
ans = []
for key, value in x.items():
    if value == 1:
        ans.append(key)
for key, value in y.items():
    if value == 1:
        ans.append(key)
print(*ans)