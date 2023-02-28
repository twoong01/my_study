import sys
input = sys.stdin.readline
n = int(input())
n_lst = list()
for i in range(n):
    n_lst.append(int(input()))
n_lst = sorted(n_lst)
for i in n_lst:
    print(i)