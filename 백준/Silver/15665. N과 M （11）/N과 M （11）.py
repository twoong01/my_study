def nPm(arr, k):
    arr = sorted(arr)
    isused = [False for _ in range(len(arr))]
    def make(chosen, isused):
        if len(chosen) == m:
            print(*chosen)
            return
        for i in range(len(arr)):
            if not isused[i] and (i == 0 or arr[i - 1] != arr[i] or isused[i - 1]):
                chosen.append(arr[i])
                make(chosen, isused)
                chosen.pop()
    make([], isused)

n, m = map(int, input().split())
n_lst = list(map(int, input().split()))
nPm(n_lst, m)