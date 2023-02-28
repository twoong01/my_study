S = int(input())
pos = 1
res = 0
while True:
    res += pos
    if res > S:
        print(pos - 1)
        break
    elif res == S:
        print(pos)
        break
    pos += 1