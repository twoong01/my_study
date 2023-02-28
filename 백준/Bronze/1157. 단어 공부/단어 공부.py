S = input()
S = S.upper()
ans = [0 for _ in range(26)]
for i in S:
    ans[ord(i)-65] += 1
mx = max(ans)
cnt = 0
for i in ans:
    if i == mx:
        cnt += 1
if cnt >= 2:
    print('?')
else:
    print(chr(ans.index(mx)+65))