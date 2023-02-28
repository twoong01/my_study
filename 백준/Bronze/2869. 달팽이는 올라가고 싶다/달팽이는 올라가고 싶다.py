from math import ceil
a,b,v = map(int, input().split())

day = ceil((v-b) / (a-b))
print(day)