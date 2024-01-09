def solution(arr):
    answer = []
    min_num = min(arr)
    arr.remove(min_num)
    if len(arr) == 0:
        return [-1]
    else:
        return arr
