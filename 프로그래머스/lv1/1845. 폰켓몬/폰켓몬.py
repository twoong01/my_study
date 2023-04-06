def solution(nums):
    answer = 0
    n = len(nums)
    p = dict()
    for i in nums:
        if i not in p:
            p.setdefault(i, 1)
        else:
            p[i] += 1
    answer = n // 2 if len(p) > n//2 else len(p)
    return answer