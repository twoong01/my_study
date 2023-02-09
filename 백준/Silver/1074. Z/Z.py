def z(n, r, c):
# 2. basecondition
    half = 2**(n - 1)
    # n == 0 일 때 return 0
    if n == 0:
        return 0
# 3. 재귀식
    # - (r, c)가 1번 사각형일 때 return func(n -1, r, c)
    # - (r, c)가 2번 사각형일 때 return func(n-1, r, c-half)
    # - (r, c)가 3번 사각형일 때 return func(n-1, r-half, c)
    # - (r, c)가 4번 사각형일 때, return func(n-1, r-half, c-half)
    else:
        if (r<half and c<half): return z(n-1, r, c)
        if (r<half and c >= half): return half*half + z(n-1, r, c-half)
        if (r >= half and c<half): return 2*half*half + z(n-1, r-half, c)
        if (r >= half and c >= half): return 3*half*half + z(n-1, r-half, c-half)

n, r, c = map(int, input().split())
print(z(n, r, c))