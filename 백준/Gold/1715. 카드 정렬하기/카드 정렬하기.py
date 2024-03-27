import heapq
import sys

n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    num = int(sys.stdin.readline())
    heapq.heappush(cards, num)

result = 0
while len(cards) > 1:
    n1 = heapq.heappop(cards)
    n2 = heapq.heappop(cards)
    result += n1 + n2
    heapq.heappush(cards, n1+n2)

print(result)