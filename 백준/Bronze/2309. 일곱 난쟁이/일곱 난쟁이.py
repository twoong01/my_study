nine = []
for _ in range(9):
    nine.append(int(input()))
nine = sorted(nine)
nine_total = sum(nine)
def find_seven(total, lst):
    for i in range(9):
        for j in range(i+1, 9):
            hap = lst[i] + lst[j]
            if total - hap == 100:
                tmp_1, tmp_2 = lst[i], lst[j]
                lst.remove(tmp_1)
                lst.remove(tmp_2)
                return lst
nine = find_seven(nine_total, nine)
for i in nine:
    print(i)