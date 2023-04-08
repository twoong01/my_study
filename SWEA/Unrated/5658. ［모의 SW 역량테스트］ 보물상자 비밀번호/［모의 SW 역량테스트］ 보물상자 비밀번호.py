t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    lst = list(input())
    l = len(lst)
    limit = l // 4
    rlt = set()
    for _ in range(limit + 1):
        for i in range(len(lst) - limit):
            a = ''.join(lst[i:i + limit])
            rlt. add(a)
        tmp = lst.pop()
        lst.insert(0, tmp)
    rlt = sorted(rlt, reverse=True)
    print(f'#{tc}', int(rlt[k - 1], 16))
