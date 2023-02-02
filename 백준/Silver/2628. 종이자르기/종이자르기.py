
w, h = map(int, input().split())
row = [0, w]
col = [0, h]
n = int(input())
for i in range(n):
    direction, number = map(int, input().split())
    if direction:
        row.append(number)
    else:
        col.append(number)
row.sort()
col.sort()

sub_row = []
sub_col = []
for i in range(len(row) - 1):
    sub_row.append(row[i + 1] - row[i])
for i in range(len(col) - 1):
    sub_col.append(col[i + 1] - col[i])
print(max(sub_row) * max(sub_col))