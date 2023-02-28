a = 42
answer = []
res = 0
l = []
for i in range(10):
    l.append(int(input()))
for i in l:
    res = i % a
    if res not in answer:
        answer.append(res)
    else:
        continue
print(len(answer))