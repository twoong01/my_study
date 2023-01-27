l = []
for i in range(28):
    l.append(int(input()))
l = sorted(l)
for i in range(1, 31):
    if i not in l:
        print(i)