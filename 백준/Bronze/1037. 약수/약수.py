k = int(input())
lst = list(map(int, input().split()))
lst = sorted(lst)
if len(lst) == 1:
    print(lst[0] ** 2)
else:
    print(lst[0] * lst[-1])