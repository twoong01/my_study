arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))
mx = 0
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > mx:
            mx = arr[i][j]
            row = i
            col = j

print(mx)
print(row+1, col+1)