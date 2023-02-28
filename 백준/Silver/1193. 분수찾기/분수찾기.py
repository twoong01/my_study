x = int(input())
total_num = 0
line = 0
while True:
    line += 1
    total_num += line
    if x <= total_num:
        break
idx = line - (total_num - x) - 1
ans = []
if line == 1:
    ans.append(f'{x}/{x}')
elif line % 2 == 0:
    for i in range(1,line+1):
        ans.append(f'{i}/{line}')
        line -= 1
else:
    for i in range(1, line+1):
        ans.append(f'{line}/{i}')
        line -= 1
print(ans[idx])
