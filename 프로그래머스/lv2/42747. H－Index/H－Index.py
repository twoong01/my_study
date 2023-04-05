def solution(citations):
    answer = 0
    
    citations.sort()
    for i in range(len(citations), -1, -1):
        if citations[-i] >= i:
            return i
    
    return answer


def solution(citations: list) -> int:
    citations.sort()
    for i in range(len(citations), -1, -1):
        if citations[-i] >= i:
            return i
    return 0