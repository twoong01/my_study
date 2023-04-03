def solution(book_time):
    answer = 0
    book_time_int = []
    for start, end in book_time:
        book_time_int.append([int(start[:2]) * 60 + int(start[3:]), 1])
        book_time_int.append([int(end[:2]) * 60 + int(end[3:]) + 10, 0])
    book_time_int.sort()
    now = 0
    for i in book_time_int:
        if i[1] == 1:
            now += 1
        else:
            now -= 1
        answer = max(answer, now)
    return answer