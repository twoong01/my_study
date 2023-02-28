keys = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = str(input())
cnt = 0
for i in range(len(S)):
    for j in keys:
        if j in S:
            S = S.replace(j, '0', 1)
            break
cnt += len(S)
print(cnt)

