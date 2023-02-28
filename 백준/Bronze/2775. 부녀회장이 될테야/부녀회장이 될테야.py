t = int(input())

for T in range(t):
    k = int(input())
    n = int(input())
    house = [[0] * n for _ in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if j == 0:
                house[i][j] = 1
            elif i == 0:
                house[i][j] = j+1
            else:
                total = 0
                for m in range(j+1):
                    total += house[i-1][m]
                house[i][j] = total
    print(house[k][n-1])