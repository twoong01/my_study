def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if not len(answer):
        return [-1]
    answer = sorted(answer)
    return answer