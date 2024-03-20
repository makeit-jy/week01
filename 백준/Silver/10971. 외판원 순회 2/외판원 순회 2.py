import sys

N = int(input()) #도시의 개수
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_cost = sys.maxsize

def dfs(start, next, cost, visited): # 시작도시번호,다음도시번호,비용,방문 도시
    global min_cost

    if len(visited) == N:
        if travel_cost[next][start] != 0:
            min_cost = min(min_cost, cost + travel_cost[next][start])
        return
    for i in range(N):
        if travel_cost[next][i] != 0 and i not in visited and cost < min_cost: 
            visited.append(i)
            dfs(start, i, cost + travel_cost[next][i], visited)
            visited.pop()

for i in range(N):
    dfs(i, i, 0, [i])

print(min_cost)