import heapq
import sys

leftHeap = []   # 최대 힙
rightHeap = []  # 최소 힙

for i in range(int(sys.stdin.readline())):
    number = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap) : 
        heapq.heappush(leftHeap, -number)
    else :
        heapq.heappush(rightHeap, number)
            
    if rightHeap and (-1 * leftHeap[0]) > rightHeap[0] :
        left = heapq.heappop(leftHeap)
        right = heapq.heappop(rightHeap)

        heapq.heappush(rightHeap, -left)
        heapq.heappush(leftHeap, -right)
    print(leftHeap[0]*-1)