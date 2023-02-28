n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
result = 0
for i in range(n):
    x = A[i]
    y = B.pop(B.index(max(B))) # pop은 인덱스 기준으로 동작하는 연산
    result += x * y
print(result)