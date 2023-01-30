a, b = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_copy = A[:]
B_copy = B[:]
A_minus = list(set(A) - set(B))
B_minus = list(set(B_copy) - set(A_copy))
print(len(A_minus) + len(B_minus))