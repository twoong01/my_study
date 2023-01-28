n, k = map(int,input().split())
stuff = list(map(int, input().split()))
cont = 0
concent = [0] * n
res = swap = num = max_l = 0
for i in stuff:
    if i in concent:
        pass
    elif 0 in concent:
        concent[concent.index(0)] = i
    else:
        for j in concent:
            if j not in stuff[num:]:
                swap = j
                break
            elif stuff[num:].index(j) > max_l:
                max_l = stuff[num:].index(j)
                swap = j
        concent[concent.index(swap)] = i
        max_l = swap = 0
        res += 1
    num += 1
print(res)
