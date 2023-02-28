t = int(input())
for i in range(t):
    grade = list(map(int, input().split()))
    avg = sum(grade[1:])/grade[0]
    cnt = 0
    for j in range(1,grade[0]+1):
        if grade[j] > avg:
            cnt += 1
    rate = (cnt/grade[0])*100
    print("{:.3f}%".format(rate))
