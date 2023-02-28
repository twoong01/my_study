import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = []
for i in range(n):
    heapq.heappush(card, int(input()))
answer = 0
while len(card) > 1:
    temp_1 = heapq.heappop(card)
    temp_2 = heapq.heappop(card)
    answer += temp_1 + temp_2
    heapq.heappush(card, temp_1 + temp_2)
print(answer)
