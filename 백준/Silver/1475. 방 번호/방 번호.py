import math

n = list(input())
num = dict()
for i in n:
    if i not in num:
        num.setdefault(i, 1)
    else:
        num[i] += 1
ans = []
tmp = 0
for key, value in num.items():
    if key == '6' or key == '9':
        tmp += value
    else:
        ans.append(value)
    ans.append(math.ceil(tmp / 2))
print(max(ans))