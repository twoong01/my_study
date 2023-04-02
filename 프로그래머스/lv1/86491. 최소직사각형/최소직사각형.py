def solution(sizes):
    answer = 0
    
    max_w = 0
    max_h = 0
    long = []
    short = []
    for i in sizes:
        long.append(max(i))
        short.append(min(i))
    max_w = max(long)
    max_h = max(short)
    answer = max_w * max_h
    return answer