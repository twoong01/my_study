import sys
input = sys.stdin.readline

def binary(target, some_list, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == some_list[mid]:
            return 1
        elif target > some_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

t = int(input())
for i in range(t):
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()
    m = int(input())
    m_list = list(map(int, input().split()))
    for j in range(len(m_list)):
        print(binary(m_list[j], n_list, 0, n-1))
