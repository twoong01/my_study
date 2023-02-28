i = 1
while True:
    p, l, v = map(int, input().split())
    if p+l+v == 0:
        break
    res = (v//l)*p
    res += min((v%l), p)
    print(f'Case {i}: {res}')
    i += 1