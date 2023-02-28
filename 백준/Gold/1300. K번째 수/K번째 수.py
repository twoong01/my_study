import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
start = 1
end = k

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for i in range(1, n+1):
        tmp += min(mid//i, n) # mid 이하의 i의 배수 or 최대 n
    if tmp >= k: # 이분 탐색 실행
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)