n, m = map(int, input().split())
isused = [False] * (n + 1)
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
        for i in range(1, n + 1):
            if not isused[i]:
                arr[k] = i
                nPm(k + 1)
nPm(0)