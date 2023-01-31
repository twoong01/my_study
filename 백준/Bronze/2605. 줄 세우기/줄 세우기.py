n = int(input())
n_lst = list(map(int, input().split()))
idx_lst = []
for idx, value in enumerate(n_lst):
    idx_lst.append([idx, value])
new = []
for i in idx_lst:
    if i == idx_lst[0]:
        new.append(i)
    else:
        new.insert(i[0] - i[1], i)
for i in new:
    print(i[0] + 1, end=' ')
