import math
n = int(input())
n_lst = list()
for _ in range(n):
    n_lst.append(int(input()))
n_lst = sorted(n_lst)
re_num = []
for i in range(1, n):
    re_num.append(n_lst[i] - n_lst[i-1])
GCD = re_num[0]
for i in range(1, len(re_num)):
    GCD = math.gcd(GCD, re_num[i])
result = set()
for i in range(2, int(math.sqrt(GCD)) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))