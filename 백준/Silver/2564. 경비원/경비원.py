w, h = map(int, input().split())
n = int(input())
shops = []
for i in range(n):
    shops.append(list(map(int, input().split())))
direc, loc = map(int, input().split())
result = 0
for i in shops:
    tmp_1, tmp_2 = 0, 0
    if i[0] == direc:
        result += abs(loc - i[1])
    else:
        if direc == 1:
            if i[0] == 2:
                tmp_1 = h + loc + i[1]
                tmp_2 = h + (w - loc) + (w - i[1])
                result += min(tmp_1, tmp_2)
            elif i[0] == 3:
                result += loc + i[1]
            else:
                result += w - loc + i[1]
        elif direc == 2:
            if i[0] == 1:
                tmp_1 = h + loc + i[1]
                tmp_2 = h + (w - loc) + (w - i[1])
                result += min(tmp_1, tmp_2)
            elif i[0] == 3:
                result += loc + h - i[1]
            else:
                result += w - loc + h - i[1]
        elif direc == 3:
            if i[0] == 1:
                result += loc + i[1]
            elif i[0] == 2:
                result += h - loc + i[1]
            else:
                tmp_1 = w + loc + i[1]
                tmp_2 = w + h - loc + h - i[1]
                result += min(tmp_1, tmp_2)
        else:
            if i[0] == 1:
                result += loc + w - i[1]
            elif i[0] == 2:
                result += h - loc + w - i[1]
            else:
                tmp_1 = w + loc + i[1]
                tmp_2 = w + h - loc + h - i[1]
                result += min(tmp_1, tmp_2)
print(result)