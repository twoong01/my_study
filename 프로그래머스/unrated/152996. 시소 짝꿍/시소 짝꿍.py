from collections import defaultdict
def solution(weights):
    answer = 0
    lst = defaultdict(int)
    # 1:1, 2:3, 1:2, 3:4
    for i in weights:
        answer += lst[i] + lst[(3*i)/2] + lst[(2*i)/3] + lst[2*i] + lst[i/2] + lst[(4*i)/3] + lst[(3*i)/4]
        lst[i] += 1
    
    return answer