from math import gcd
def solution(arrayA, arrayB):
    answer = 0
    gcd_A, gcd_B = check_mine(arrayA), check_mine(arrayB)
    rlt1, rlt2 = find_answer(gcd_A, arrayB), find_answer(gcd_B, arrayA)
    answer = max(answer, rlt1, rlt2)
    return answer
def check_mine(arr1):
    GCD = 0
    for i in range(len(arr1)):
        GCD = gcd(GCD, arr1[i])
    return GCD

def find_answer(GCD, arr):
    for i in arr:
        if i % GCD == 0:
            return 0
    return GCD
        
        