from itertools import combinations
n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))
cnt = 0
house = []
chicken = []
chosen = []
part_chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        elif city[i][j] == 1:
            house.append([i, j])
result = 1e9
for i in combinations(chicken, m):
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] - i[j][0]) + abs(h[1] - i[j][1]))
        temp += chi_len
    result = min(result, temp)
print(result)