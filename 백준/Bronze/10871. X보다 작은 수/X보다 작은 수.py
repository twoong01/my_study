n, a = map(int, input().split())
l = list(map(int, input().split()))
answer = []
for i in l:
    if i < a:
        answer.append(i)
        
print(*answer)