import sys
import heapq as hq

cnt = int(sys.stdin.readline().strip())
heap = []

for _ in range(cnt):
  x = int(sys.stdin.readline().strip())

  if x: # x가 0이 아닌 경우    
    hq.heappush(heap, (-x))
    # heapq 모듈에서는 최소 힙(Min Heap)만을 지원함.
    # 하지만 문제는 최대힙을 구현해야함.
    # 따라서 음수로 만듦으로써 최대값을 출력할 수 있다.
  
  else: # x가 0인 경우    
    try: # 힙에 요소가 있는 경우      
      print(-1 * hq.heappop(heap)) # 음수로 저장되어 있으므로 -1을 곱해 최대값 출력
    
    except: # 힙에 요소가 없는 경우
      print(0)