from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque([0 for _ in range(bridge_length)])
    sum_q = 0
    while q:
        answer += 1
        now = q.popleft()
        sum_q -= now
        
        if truck_weights:
            if sum_q + truck_weights[0] <= weight:
                sum_q += truck_weights[0]
                q.append(truck_weights[0])
                truck_weights.pop(0)
            else:
                q.append(0)
    return answer