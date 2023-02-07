n, k = map(int, input().split())
n_lst = list(map(int, input().split()))
tmp_sum = []
tmp_sum.append(sum(n_lst[:k]))

for i in range(n - k):
    tmp_sum.append(tmp_sum[i] - n_lst[i] + n_lst[i + k])
print(max(tmp_sum))