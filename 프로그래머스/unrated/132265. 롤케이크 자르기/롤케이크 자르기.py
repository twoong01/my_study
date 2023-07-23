def solution(topping):
    answer = 0
    left = set()
    right = dict()
    for i in topping:
        right[i] = right.get(i, 0)
        right[i] += 1
    for i in topping:
        left.add(i)
        right[i] -= 1
        if right[i] == 0:
            del right[i]
        if len(left) == len(right):
            answer += 1
    return answer