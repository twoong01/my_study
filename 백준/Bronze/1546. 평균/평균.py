n = int(input())
grade = list(map(int, input().split()))
mx = max(grade)
for i in range(len(grade)):
    grade[i] = grade[i]/mx*100
print(sum(grade)/n)