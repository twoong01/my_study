import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [(-1) * work for work in works]
    heapq.heapify(works)
    for i in range(n):
        cur_work = heapq.heappop(works)
        cur_work += 1
        heapq.heappush(works, cur_work)
    return sum([(work)**2 for work in works])