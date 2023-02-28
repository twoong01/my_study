import sys
T = int(input())
for i in range(T):
    cnt = 1
    people_data = []
    N = int(input())
    for j in range(N):
        A, B = map(int, sys.stdin.readline().split())
        people_data.append([A, B])
        
    people_data.sort()
    Max = people_data[0][1]
    for k in range(1, N):
        if Max > people_data[k][1]:
            Max = people_data[k][1]
            cnt += 1
    print(cnt)