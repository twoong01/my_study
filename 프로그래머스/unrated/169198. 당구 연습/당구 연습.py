def solution(m, n, startX, startY, balls):
    answer = []
    
    points = []
    points.append((-startX, startY))
    points.append((2*m-startX, startY))
    points.append((startX, -startY))
    points.append((startX, 2*n-startY))
    for b in balls:
        x1, y1 = b[0], b[1]
        min_dis = m**2 + n**2
        for i, p in enumerate(points):
            x2, y2 = p[0], p[1]
            dx = x2- x1
            dy = y2- y1
            if i == 0 and dy == 0 and abs(x1) <= abs(x2):
                continue
            elif i == 1 and dy == 0 and abs(m-x1) <= abs(m-x2):
                continue
            elif i == 2 and dx == 0 and abs(y1) <= abs(y2):
                continue
            elif i == 3 and dx == 0 and abs(n-y1) <= abs(n-y2):
                continue
            dx = dx**2
            dy = dy**2
            dd = (dx + dy)
            if min_dis > dd:
                min_dis = dd
        answer.append(min_dis)
    return answer