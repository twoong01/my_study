def recursion(s, l, r, cnt):
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else:
        cnt += 1 
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s, cnt):
    return recursion(s, 0, len(s)-1, cnt)
t = int(input())
for T in range(t):
    cnt = 1
    s = str(input())
    print(*isPalindrome(s, cnt))