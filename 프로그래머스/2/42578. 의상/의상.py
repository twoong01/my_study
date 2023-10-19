def solution(clothes):
    answer = 1;
    closet = {}
    for cloth in clothes:
        if cloth[1] not in closet:
            closet.setdefault(cloth[1], 1)
        else:
            closet[cloth[1]] += 1
    for key, value in closet.items():
        answer *= (value + 1)
    return answer - 1