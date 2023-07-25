def solution(n):
    answer = 0
    value = str(n ** 0.5)
    check = len(value[value.find('.') + 1:])
    if check == 1:
        return (float(value) + 1) ** 2
    else:
        return -1