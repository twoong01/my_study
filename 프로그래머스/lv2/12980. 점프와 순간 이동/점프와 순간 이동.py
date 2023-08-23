def solution(n):
    ans = 0
    while True:
        if n % 2:
            ans += 1
            n //= 2
        else:
            n //= 2
        
        if n == 0:
            return ans