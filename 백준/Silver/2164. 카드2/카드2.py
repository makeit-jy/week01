from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()
queue = deque(range(1,n+1))
while len(queue) > 1: # 큐에 요소가 하나 남을 때까지 반복
    queue.popleft()
    queue.append(queue.popleft())
print(queue.popleft())

# 뽑고 버리고, 뽑고 밑에 넣으므로 -> 큐에 적어도 2개가 있어야 함