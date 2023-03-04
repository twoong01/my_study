import heapq
import sys
input = sys.stdin.readline

N = int(input())
left_heap = []
right_heap = []
for i in range(N):
    n = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -n)
    else:
        heapq.heappush(right_heap, n)

    if right_heap and right_heap[0] < -left_heap[0]:
        right = heapq.heappop(right_heap)
        left = heapq.heappop(left_heap)

        heapq.heappush(left_heap, -right)
        heapq.heappush(right_heap, -left)
    print(-left_heap[0])