def solution(n):
    answer = 0

    numbers = list(map(int, str(n)))
    for i in numbers:
        answer += i

    return answer