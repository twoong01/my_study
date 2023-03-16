
n, m = map(int, input().split())
n_lst = [list(map(int, input().split())) for _ in range(n)]
n_lst2 = list(zip(*n_lst))
figure1 = [] # 직선
figure2 = [] # 정사각형
figure3 = [] # L형
figure4 = [] # ㄹ형
figure5 = [] # ㅗ형

# 직선
for i in range(n):
    for j in range(m-3):
        figure1.append(sum(n_lst[i][j:j+4]))
for i in range(m):
    for j in range(n-3):
        figure1.append(sum(n_lst2[i][j:j+4]))

# 정사각형
for i in range(n-1):
    for j in range(m-1):
        figure2.append(sum(n_lst[i][j:j+2]) + sum(n_lst[i+1][j:j+2]))

# L형
for i in range(n-1):
    for j in range(m - 2):
        figure3.append(sum(n_lst[i][j:j+3]) + n_lst[i+1][j])
        figure3.append(sum(n_lst[i][j:j+3]) + n_lst[i+1][j+2])

for i in range(1, n):
    for j in range(m - 2):
        figure3.append(sum(n_lst[i][j:j+3]) + n_lst[i-1][j])
        figure3.append(sum(n_lst[i][j:j+3]) + n_lst[i-1][j+2])


for i in range(m-1):
    for j in range(n - 2):
        figure3.append(sum(n_lst2[i][j:j+3]) + n_lst2[i+1][j])
        figure3.append(sum(n_lst2[i][j:j+3]) + n_lst2[i+1][j+2])


for i in range(1, m):
    for j in range(n - 2):
        figure3.append(sum(n_lst2[i][j:j+3]) + n_lst2[i-1][j])
        figure3.append(sum(n_lst2[i][j:j+3]) + n_lst2[i-1][j+2])

# ㄹ형
for i in range(n-1):
    for j in range(m-2):
        figure4.append(sum(n_lst[i][j:j+2]) + sum(n_lst[i+1][j+1:j+3]))
        figure4.append(sum(n_lst[i+1][j:j+2]) + sum(n_lst[i][j+1:j+3]))
for i in range(m-1):
    for j in range(n-2):
        figure4.append(sum(n_lst2[i][j:j+2]) + sum(n_lst2[i+1][j+1:j+3]))
        figure4.append(sum(n_lst2[i+1][j:j+2]) + sum(n_lst2[i][j+1:j+3]))

# ㅗ형
for i in range(n-1):
    for j in range(m-2):
        figure5.append(sum(n_lst[i][j:j+3]) + n_lst[i+1][j+1])
for i in range(m-1):
    for j in range(n-2):
        figure5.append(sum(n_lst2[i][j:j+3]) + n_lst2[i+1][j+1])
for i in range(1, n):
    for j in range(m-2):
        figure5.append(sum(n_lst[i][j:j+3]) + n_lst[i-1][j+1])
for i in range(1, m):
    for j in range(n-2):
        figure5.append(sum(n_lst2[i][j:j+3]) + n_lst2[i-1][j+1])


ans = []
ans.extend(figure1)
ans.extend(figure2)
ans.extend(figure3)
ans.extend(figure4)
ans.extend(figure5)
print(max(ans))