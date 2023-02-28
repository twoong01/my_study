k = int(input())
t = list(map(int, input().split()))
t.sort()
sum1 = 0
sum2 = 0

for i in t:
    sum1 += i
    sum2 += sum1
print(sum2)