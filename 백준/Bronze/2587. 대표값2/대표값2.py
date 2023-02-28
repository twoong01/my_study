lst = []
for i in range(5):
    lst.append(int(input()))
print(int(sum(lst)/5))
lst = sorted(lst)
print(lst[2])