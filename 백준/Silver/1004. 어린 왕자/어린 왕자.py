t = int(input())
for T in range(t):    
    x1, y1, x2, y2 = map(int, input().split())
    cnt = int(input())
    lst = []
    for i in range(cnt):
        lst.append(list(map(int, input().split())))
    check_1 = set()
    check_2 = set()
    for i in range(cnt):
        distance_1 = ((x1 - lst[i][0]) ** 2 + (y1 - lst[i][1]) ** 2)
        distance_2 = ((x2 - lst[i][0]) ** 2 + (y2 - lst[i][1]) ** 2)
        if distance_1 < (lst[i][2])**2:
            check_1.add(i)
        if distance_2 < (lst[i][2])**2:
            check_2.add(i)
        
    print(len((check_1|check_2) - (check_1&check_2)))