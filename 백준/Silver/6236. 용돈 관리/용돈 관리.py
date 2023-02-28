import sys
input = sys.stdin.readline

n, m = map(int, input().split())
datas = []
for i in range(n):
    datas.append(int(input()))
start = 0
end = int(1e9)
answer = int(1e9)
while start <= end:
    mid = (start + end) // 2
    count, money = 0, 0
    lack = False

    for d in datas:
        if mid - d < 0:
            # 돈을 뽑아도 하루를 못넘기면
            lack = True
        elif money - d < 0:
            money = mid
            count += 1
        money -= d
    if not lack:
        if count <= m:
            end = mid - 1
            if mid < answer:
                answer = mid
        elif count > m:
            start = mid + 1
    else:
        start = mid + 1
print(answer)
