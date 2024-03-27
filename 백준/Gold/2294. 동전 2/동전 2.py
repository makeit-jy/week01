from collections import deque
import sys

n, value = map(int, sys.stdin.readline().split())
coins = list(set(int(sys.stdin.readline()) for _ in range(n)))

def bfs(coins, value):
    queue = deque()
    visited = [False] * (value + 1)  # 방문 여부를 나타내는 배열

    for coin in coins:
        if coin <= value:  # 동전의 가치가 목표값보다 작거나 같은 경우만 고려
            queue.append((coin, 1))
            visited[coin] = True

    while queue:
        total, cnt = queue.popleft()

        if total == value:
            return cnt

        for coin in coins:
            total_next = total + coin
            if total_next <= value and not visited[total_next]:
                queue.append((total_next, cnt + 1))
                visited[total_next] = True

    return -1

result = bfs(coins, value)
print(result)