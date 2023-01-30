k = int(input())
lst = []
for i in range(6):
    lst.append(list(map(int, input().split())))
bigbox, smallbox = 0, 0
direction = dict()
for i in range(len(lst)):
    if lst[i][0] in direction:
        direction[lst[i][0]] += 1
    else:
        direction.setdefault(lst[i][0], 1)
box = []
for key, value in direction.items():
    if value == 1:
        box.append(key)

w, h, small_w, small_h = 0, 0, 0, 0
for i in range(2):
    for j in range(6):
        if lst[j][0] == box[i]:
            if i == 0:
                try:
                    w = lst[j][1]
                    small_w = lst[j+3][1]
                except:
                    w = lst[j][1]
                    small_w = lst[j-3][1]
            else:
                try:
                    h = lst[j][1]
                    small_h = lst[j+3][1]
                except:
                    h = lst[j][1]
                    small_h = lst[j - 3][1]
bigbox = w * h
smallbox = small_w * small_h
ans = (bigbox - smallbox) * k
print(ans)