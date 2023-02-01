import sys
input = sys.stdin.readline
n = int(input())
n_lst = list(map(int, input().split()))
n_lst = sorted(n_lst)
m = int(input())
m_lst = list(map(int, input().split()))
for i in m_lst:
    start, end = 0, len(n_lst) - 1
    while True:
        if start > end:
            print(0)
            break
        mid = (start + end) //2
        if n_lst[mid] == i:
            print(1)
            break
        elif n_lst[mid] > i:
            end = mid -1
        else:
            start = mid + 1
