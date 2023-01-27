n = int(input())
x_lst = list(map(int, input().split()))
tmp = []
for idx, value in enumerate(x_lst):
    tmp.append([idx, value])
tmp = sorted(tmp, key=lambda x : x[1])
cnt = 0
tmp_value = 0
for i in range(len(tmp)):
    if i == 0:
        tmp_value = tmp[i][1]
        tmp[i][1] = cnt
        cnt += 1
    elif tmp_value == tmp[i][1]:
        tmp_value = tmp[i][1]
        tmp[i][1] = cnt - 1
    else:
        tmp_value = tmp[i][1]
        tmp[i][1] = cnt
        cnt += 1
tmp = sorted(tmp, key=lambda x : x[0])
for i in range(len(tmp)):
    print(tmp[i][1], end=' ')