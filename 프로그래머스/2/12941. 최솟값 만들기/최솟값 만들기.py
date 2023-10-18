def solution(A,B):
    answer = 0
    sorted_A = sorted(A)
    sorted_B = sorted(B, reverse=True)
    for i in range(len(A)):
        answer += sorted_A[i] * sorted_B[i]
    return answer