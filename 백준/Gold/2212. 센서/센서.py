n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()
if k < n:
    diff_arr = []
    for i in range(len(arr) - 1):
        diff_arr.append(abs(arr[i] - arr[i + 1]))
    diff_arr.sort(reverse=True)

    ans = sum(diff_arr[k-1:])
    print(ans)
else:
    print(0)