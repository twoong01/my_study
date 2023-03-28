t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    table = []
    for _ in range(n):
        s, e = map(int, input().split())
        table.append((s, e))
    table = sorted(table, key=lambda x : x[1])
    ans = []
    for i in table:
        if len(ans) == 0:
            ans.append(i)
        else:
            if ans[-1][1] <= i[0]:
                ans.append(i)
    print(f'#{tc}', len(ans))