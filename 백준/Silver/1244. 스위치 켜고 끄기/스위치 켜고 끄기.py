n = int(input())
switch_lst = list(map(int, input().split()))
student = int(input())
for i in range(student):
    gender, number = map(int, input().split())
    if gender == 1: # 남자일때
        for j in range(1, n + 1):
            if j % number == 0:
                if switch_lst[j - 1] == 1:
                    switch_lst[j - 1] = 0
                else:
                    switch_lst[j - 1] = 1
    else: # 여자일때
        if number != 1 and number != n:
            change_lst = set()
            for x in range(number):
                if (number - x) > 0 and (number + x) < n + 1:
                    if switch_lst[number - x - 1] == switch_lst[number + x - 1]:
                        change_lst.add(number - x)
                        change_lst.add(number + x)
                    else:
                        break
                else:
                    break
        else:
            change_lst = {number}
        for j in change_lst:
            if switch_lst[j - 1] == 1:
                switch_lst[j - 1] = 0
            else:
                switch_lst[j - 1] = 1
for i in range(len(switch_lst)):
    print(switch_lst[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
