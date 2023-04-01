t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    mx_stock = max(lst)
    profit = 0
    mx = 0
    for i in range(n - 1, -1, -1):
        if mx < lst[i]:
            mx = lst[i]
        elif mx > lst[i]:
            profit += (mx - lst[i])

    print(profit)