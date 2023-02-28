# 문제 해결 아이디어 : 누적합
import sys
input = sys.stdin.readline
def binary(data_list, x):
    start = 0
    end = len(data_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if data_list[mid] <= x:
            start = mid + 1
        else:
            end = mid - 1
    return len(data_list) - (end + 1)

n, H = map(int, input().split())
down = []
up =  []
for i in range(n):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))
down.sort()
up.sort()
ans = n
cnt = 0

for h in range(1, H + 1):
    down_num = binary(down, h - 1)
    up_num = binary(up, H - h)
    cur_num = down_num + up_num
    if cur_num < ans:
        ans = cur_num
        cnt = 1
    elif cur_num == ans:
        cnt += 1
print(ans, cnt)