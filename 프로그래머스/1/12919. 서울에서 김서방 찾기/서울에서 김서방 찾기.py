def solution(seoul):
    answer = ''
    place = 0
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            place = i
    answer = f'김서방은 {place}에 있다'
    return answer