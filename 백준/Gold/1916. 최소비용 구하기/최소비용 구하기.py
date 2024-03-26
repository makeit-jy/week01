import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        dist, now = heapq.heappop(queue)

        if (distance[now] < dist):
            continue

        for cityInfo in graph[now]: # 연결된 도시 번호들
            
            city, cost = cityInfo[0], cityInfo[1]

            cost  = dist + cost
            if distance[city] > cost:
                distance[city] = cost
                heapq.heappush(queue,[cost, city])


graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int,sys.stdin.readline().split())
    graph[start].append([end, cost])

start, end = map(int,sys.stdin.readline().split())

distance = [INF]*(n+1)
dijkstra(start)

print(distance[end])