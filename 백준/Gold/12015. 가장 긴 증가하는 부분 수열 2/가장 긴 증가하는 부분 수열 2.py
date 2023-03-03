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
        # find the index to insert the current element in the LIS
        l, r = 0, len(lis)-1
        idx = -1
        while l <= r:
            mid = (l + r) // 2
            if lis[mid] >= n_lst[i]:
                idx = mid
                r = mid - 1
            else:
                l = mid + 1
        if idx != -1:
            lis[idx] = n_lst[i]
        else:
            lis[0] = n_lst[i]
print(len(lis))
