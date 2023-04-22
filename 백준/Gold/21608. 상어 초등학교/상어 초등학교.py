n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]
maps = [[0] * n for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for order in range(n**2):
    student = students[order]
    # 가능한 자리를 다 담아서 정렬 후 앉힘
    tmp = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0:
                like = 0
                blank = 0
                # 주변 탐색
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if not( 0 <= nx < n and 0 <= ny < n): continue
                    # 좋아하는 학생이 있는 경우
                    if maps[nx][ny] in student[1:]:
                        like += 1
                    # 빈공간인 경우
                    if not maps[nx][ny]:
                        blank += 1
                tmp.append([like, blank, i, j])
    tmp.sort(key=lambda x : [-x[0], -x[1], x[2], x[3]])
    maps[tmp[0][2]][tmp[0][3]] = student[0]

total = 0
students.sort()
for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if maps[nx][ny] in students[maps[i][j] - 1]:
                ans += 1
        if ans == 0 or ans == 1:
            total += ans
        else:
            total += 10**(ans - 1)
print(total)