n = int(input())
lst = list(map(int, input().split()))

if n == 1 or (n == 2 and lst[0] != lst[1]):
    print('A')
elif n == 2 and lst[0] == lst[1]:
    print(lst[0])
else:
    if lst[0] - lst[1] == 0:
        a = 0
    else:
        a = (lst[1] - lst[2]) // (lst[0] - lst[1])
    b = lst[1] - a*lst[0]
    flag = True
    for i in range(n - 1):
        if lst[i + 1] != lst[i] * a + b:
            flag = False
    if flag:
        print(lst[-1] * a + b)
    else:
        print('B')