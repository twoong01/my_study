from itertools import permutations
from copy import deepcopy

n, m, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
rotate = [list(map(int, input().split())) for _ in range(t)]

ans = 1e9

for ch in permutations(rotate, t):
    copy_map = deepcopy(maps)
    for r, c, s in ch:
        r -= 1
        c -= 1
        for k in range(s, 0, - 1):
            tmp = copy_map[r - k][c + k]
            copy_map[r - k][c - k + 1 : c + k + 1] = copy_map[r - k][c - k : c + k]
            for row in range(r - k, r + k):
                copy_map[row][c - k] = copy_map[row + 1][c - k]
            copy_map[r + k][c - k : c + k] = copy_map[r + k][c - k + 1 : c + k + 1]
            for row in range(r + k, r - k, -1):
                copy_map[row][c + k] = copy_map[row - 1][c + k]
            copy_map[r - k + 1][c + k] = tmp
    for row in copy_map:
        ans = min(ans, sum(row))
print(ans)