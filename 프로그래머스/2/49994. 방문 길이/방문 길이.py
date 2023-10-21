def solution(dirs):
    answer = 0
    dir = {
        "U" : (0, -1),
        "D" : (0, 1),
        "R" : (1, 0),
        "L" : (-1, 0)
    }
    x, y = 5, 5
    visited = []
    for d in dirs:
        nx = x + dir[d][0]
        ny = y + dir[d][1]
        if not (0 <= nx <= 10 and 0 <= ny <= 10): continue
        visited.append((x, y, nx, ny))
        visited.append((nx, ny, x, y))
        x, y = nx, ny
    mapSet = set(visited)
    answer = len(mapSet) // 2
    return answer