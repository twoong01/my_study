n = int(input())
weight = list(map(int, input().split()))
weight.sort()
total = 0
for i in range(n):
    if total + 1 >= weight[i]:
        total += weight[i]
    else:
        break
print(total + 1)
