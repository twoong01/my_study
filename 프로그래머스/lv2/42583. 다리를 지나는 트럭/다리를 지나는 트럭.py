from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = deque([0] * bridge_length)
    sum_q = 0
    while q:
        answer += 1
        node = q.popleft()
        sum_q -= node
        
        if truck_weights:
            if sum_q + truck_weights[0] > weight:
                q.append(0)
            else:
                sum_q += truck_weights[0]
                q.append(truck_weights.pop(0))
    return answer