lst = list(map(int, input().split()))
while sum(lst) != 0:
    lst = sorted(lst)
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2: 
        print('right')
    else:
        print('wrong')
    lst = list(map(int, input().split()))


