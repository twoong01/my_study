n = 1000 - int(input())
cnt = 0
change = [500, 100, 50, 10, 5, 1]
for i in range(len(change)):
    while(n - change[i] >= 0):
        n -= change[i]
        cnt += 1
print(cnt)