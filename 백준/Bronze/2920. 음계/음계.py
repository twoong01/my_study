lst = list(map(int, input().split()))
tmp = lst[1] - lst[0]
if tmp > 0:
    for i in range(1, len(lst)):
        if i == 1:
            continue
        else:
            if lst[i] - lst[i-1] == tmp:
                pass
            else:
                print('mixed')
                break
    else:
        print('ascending')
else:
    for i in range(1, len(lst)):
        if i == 1:
            continue
        else:
            if lst[i] - lst[i-1] == tmp:
                pass
            else:
                print('mixed')
                break
    else:
        print('descending')