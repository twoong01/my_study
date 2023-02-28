import sys
n = int(sys.stdin.readline())
people = []
for i in range(n):
    people.append(list(sys.stdin.readline().split()))

people.sort(key=lambda x:int(x[0]))
for i in people:
    print(i[0], i[1])