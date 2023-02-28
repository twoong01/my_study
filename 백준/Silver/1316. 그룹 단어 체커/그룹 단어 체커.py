n = int(input())
cnt = 0
for i in range(n):
    temp = dict()
    tmp = 0
    group = list()
    word = input()
    for j in range(len(word)):
        group.append(word[j])

    for k in range(len(group)):
        if k == 0:
            bf_word = group[k]
            temp[group[k]] = 1
            continue
        else:
            if bf_word != group[k]:
                bf_word = group[k]
                if group[k] not in temp:
                    temp[group[k]] = 1
                    tmp += 1
                    continue
                else:
                    continue
            else:
                temp[group[k]] += 1
                tmp += 1
                pass
    if sum(temp.values()) == len(group):
        cnt += 1
print(cnt)