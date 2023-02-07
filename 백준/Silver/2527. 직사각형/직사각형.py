for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if (x1 > p2) or (y1 > q2) or (p1 < x2) or (q1 < y2):
        print('d')
    elif (x1 == p2 and y1 == q2) or (p1 == x2 and y1 == q2) or (p1 == x2 and q1 == y2) or (x1 == p2 and q1 == y2):
        print('c')
    elif (y1 == q2 and (x2 in range(x1, p1 + 1) or p2 in range(x1, p1 + 1))) or (q1 == y2 and (x2 in range(x1, p1 + 1) or p2 in range(x1, p1 + 1)))\
        or (x1 == p2 and (y2 in range(y1, q1 + 1) or q2 in range(y1, q1 + 1))) or (x2 == p1 and (y2 in range(y1, q1 + 1) or q2 in range(y1, q1 + 1)))\
            or (y1 == q2 and (x1 in range(x2, p2 + 1) or p1 in range(x2, p2 + 1))) or (q1 == y2 and (x1 in range(x2, p2 + 1) or p1 in range(x2, p2 + 1))) \
            or (x1 == p2 and (y1 in range(y2, q2 + 1) or q1 in range(y2, q2 + 1))) or (x2 == p1 and (y1 in range(y2, q2 + 1) or q1 in range(y2, q2 + 1))):
        print('b')
    else:
        print('a')