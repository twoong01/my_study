def binary_left(start, end, target):
    global idx
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] >= target:
            idx = mid
            end = mid - 1
        else:
            start = mid + 1
    return start

n = int(input())
n_lst = list(map(int, input().split()))

# O(nlogn)
dp = [1]
lis = [n_lst[0]]
for i in range(1, len(n_lst)):
    if n_lst[i] > lis[-1]:
        lis.append(n_lst[i])
        dp.append(dp[-1] + 1)
    else:
        idx = binary_left(0, len(lis) - 1, n_lst[i])
        lis[idx] = n_lst[i]
print(len(lis))