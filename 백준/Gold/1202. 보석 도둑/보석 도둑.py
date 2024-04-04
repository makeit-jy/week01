import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
gem = []
for _ in range(N):
    weight, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(gem, (weight, cost))

bags = []
for _ in range(K):
    w = int(sys.stdin.readline())
    bags.append(w)
bags.sort()

result = 0
temp = []
for bag_weight in bags:
    while gem:
        if bag_weight >= gem[0][0]:
            weight, cost = heapq.heappop(gem)
            heapq.heappush(temp, -cost)
        else:
            break
    if temp:
        result -= heapq.heappop(temp)
print(result)