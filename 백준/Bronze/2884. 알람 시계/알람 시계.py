h, m = map(int, input().split())
if m < 45 and h == 0:
    h = 23
    m = 60 - (45-m)
elif m < 45:
    h = h - 1
    m = 60 - (45 - m)
else:
    m = m - 45
print(h, m)