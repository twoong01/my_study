n, k = map(int, input().split())
girls = []
boys = []
for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        girls.append(tmp)
    else:
        boys.append(tmp)
girls_dict, boys_dict = dict(), dict()
for i in girls:
    if i[1] in girls_dict:
        girls_dict[i[1]] += 1
    else:
        girls_dict.setdefault(i[1], 1)
for i in boys:
    if i[1] in boys_dict:
        boys_dict[i[1]] += 1
    else:
        boys_dict.setdefault(i[1], 1)
cnt = 0
for value in girls_dict.values():
    if value > k:
        cnt += (value // k) + 1
    else:
        cnt += 1

for value in boys_dict.values():
    if value > k:
        cnt += (value // k) + 1
    else:
        cnt += 1

print(cnt)
