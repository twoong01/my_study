n, m = map(int, input().split())
n_lst = list(map(int, input().split()))
n_lst = sorted(n_lst)
isused = [False] * n
arr = [0] * m
def nPm(k):
    if k == m:
        if arr != sorted(arr):
            return
        else:
            for i in range(m):
                print(arr[i], end=' ')
        print()
        return
    else:
        for idx, value in enumerate(n_lst):
            if not isused[idx]:
                arr[k] = value
                nPm(k + 1)
nPm(0)