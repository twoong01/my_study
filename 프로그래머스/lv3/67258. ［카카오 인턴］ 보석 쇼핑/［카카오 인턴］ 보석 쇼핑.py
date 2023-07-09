def solution(gems):
    answer = [0, len(gems)] # 초기에 가장 긴 배열을 주고 비교하기 위함
    left, right = 0, 0 # 투 포인터
    size = len(set(gems)) # 보석 종류 갯수
    dict_gems = {gems[0] : 1}
    while left < len(gems) and right < len(gems):
        if len(dict_gems) == size: # 모든 보석이 dict에 들어갔다면
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                dict_gems[gems[left]] -= 1
                if dict_gems[gems[left]] == 0:
                    del dict_gems[gems[left]]
                left += 1
        else:
            right += 1
            
            if right == len(gems):
                break
            dict_gems[gems[right]] = dict_gems.get(gems[right], 0) + 1
    answer = [answer[0] + 1, answer[1] + 1]
    return answer