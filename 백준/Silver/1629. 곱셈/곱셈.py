A, B, C = map(int, input().split())

def multi(A, B, C):
    if B == 1:
        return A % C
    val = multi(A, B // 2, C)
    val = val * val % C
    if B % 2 == 0:
        return val
    else:
        return val * A % C

print(multi(A, B, C))