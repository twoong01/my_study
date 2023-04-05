def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key=lambda x : str(x) * 3, reverse=True)
    ans = ''.join(str(i) for i in numbers)
    
    return '0' if ans[0] == '0' else ans