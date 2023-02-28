import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
nutrients = [[5] * n for _ in range(n)]
plus = [list(map(int, input().split())) for _ in range(n)]
tree_age = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y, age = map(int, input().split())
    tree_age[x - 1][y - 1] =  [age]
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
dead = []

def spring():
    global dead
    for i in range(n):
         for j in range(n):
            if type(tree_age[i][j]) == list:
                tree_age[i][j].sort()
                for l in range(len(tree_age[i][j])):
                    if nutrients[i][j] >= tree_age[i][j][l]:
                        nutrients[i][j] -= tree_age[i][j][l]
                        tree_age[i][j][l] += 1
                    else:
                        dead[i][j] = tree_age[i][j][l:]
                        del tree_age[i][j][l:]
                        break

def summer(dead):
    for i in range(n):
         for j in range(n):
            if type(dead[i][j]) == list:
                for k in range(len(dead[i][j])):
                    nutrients[i][j] += int(dead[i][j][k]//2)

def fall():
    for i in range(n):
         for j in range(n):
            if type(tree_age[i][j]) == list:
                for k in range(len(tree_age[i][j])):
                    if tree_age[i][j][k] % 5 == 0:
                        for l in range(8):
                                nx = i + dx[l]
                                ny = j + dy[l]
                                if not(0 <= nx < n and 0 <= ny < n): continue
                                if tree_age[nx][ny] == 0:
                                    tree_age[nx][ny] = [1]
                                else:
                                    tree_age[nx][ny].append(1)

def winter():
    for i in range(n):
         for j in range(n):
            nutrients[i][j] += plus[i][j]
for year in range(k):
    dead = [[0] * n for _ in range(n)]
    spring()
    summer(dead)
    fall()
    winter()
_sum = 0
for i in range(n):
    for j in range(n):
        if type(tree_age[i][j]) == list:
            _sum += len(tree_age[i][j])
print(_sum)