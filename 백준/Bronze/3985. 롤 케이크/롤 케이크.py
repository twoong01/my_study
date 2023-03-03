L = int(input())
n = int(input())
cake = [0] * L
people = []
mx = 0
mx_id = 0
for i in range(n):
    start, end = map(int, input().split())
    if mx < end - start:
        mx = end - start
        mx_id = i + 1
    for j in range(start - 1, end):
        if cake[j] == 0:
            cake[j] = i + 1
for i in range(1, n + 1):
    people.append(cake.count(i))
print(mx_id)
print(people.index(max(people)) + 1)