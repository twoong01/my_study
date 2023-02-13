n = int(input())
n_lst = sorted(set(map(int, input().split())))
print(*n_lst)