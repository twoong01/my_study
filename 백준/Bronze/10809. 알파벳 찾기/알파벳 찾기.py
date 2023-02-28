S = input()
ans = [-1 for _ in range(26)]
for i in S:
    ans[ord(i)-97] = S.index(i)
print(*ans)