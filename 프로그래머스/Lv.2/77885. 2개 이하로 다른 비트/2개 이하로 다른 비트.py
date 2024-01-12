def solution(numbers):
    answer = []
    for number in numbers:
        num = number
        cnt = 0
        while number % 2:
            cnt += 1
            number //= 2
        answer.append(num + 2**(cnt - 1) if cnt != 0 else num + 1)
    return answer