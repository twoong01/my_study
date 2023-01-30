n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
check = dict()
for i in n_lst:
    if i in check:
        check[i] += 1
    else:
        check.setdefault(i, 1)
for i in m_lst:
    if i in check:
        print(check[i], end=' ')
    else:
        print(0, end=' ')
