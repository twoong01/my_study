x, y, z = map(int, input().split())
prize = 0
if x == y == z:
    prize = 10000 + x*1000
    print(prize)
elif x == z:
    prize = 1000 + x*100
    print(prize)
elif x == y:
    prize = 1000 + x*100
    print(prize)
elif y == z:
    prize = 1000 + y*100
    print(prize)
else:
    prize = max(x, y, z)*100
    print(prize)