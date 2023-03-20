n = int(input())
home = []
all_p = 0
for _ in range(n):
    idx, p = map(int, input().split())
    home.append((idx, p))
    all_p += p
home.sort(key=lambda x : x[0])

count = 0
for i in range(n):
    count += home[i][1]
    if count >= all_p/2:
        print(home[i][0])
        break