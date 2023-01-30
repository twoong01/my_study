s = input()
ans = set(s)
for i in range(len(s)):
    for j in range(len(s) - i):
        ans.add(s[j:j+i+1])
print(len(ans))