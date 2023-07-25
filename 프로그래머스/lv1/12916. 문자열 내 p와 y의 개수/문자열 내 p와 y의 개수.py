def solution(s):
    answer = True
    p_count = s.upper().count('P')
    y_count = s.upper().count('Y')
    if p_count == y_count:
        return True
    else:
        return False