n = int(input())
n_lst = list(map(int, input().split()))

length1, length2 = 0, 0
tmp = n_lst[0]
bigger, smaller = [], []
for i in range(n):
    if not bigger:
        bigger.append(n_lst[i])
    else:
        if bigger[-1] <= n_lst[i]:
            bigger.append(n_lst[i])
        else:
            if length1 < len(bigger):
                length1 = len(bigger)
            bigger = []
            bigger.append(n_lst[i])

    if not smaller:
        smaller.append(n_lst[i])
    else:
        if smaller[-1] >= n_lst[i]:
            smaller.append(n_lst[i])
        else:
            if length2 < len(smaller):
                length2 = len(smaller)
            smaller = []
            smaller.append(n_lst[i])
max_list = max(len(smaller), len(bigger))
print(max(max(length1, length2), max_list))