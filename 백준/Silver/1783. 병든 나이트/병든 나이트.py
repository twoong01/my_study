n, m = map(int, input().split())
if n == 1:
    count = 1
elif n == 2:
    count = min(4,(m-1)//2 + 1)
elif m < 7:
    count = min(4, m)
else:
    count = (2 + (m - 5)) + 1
print(count)
