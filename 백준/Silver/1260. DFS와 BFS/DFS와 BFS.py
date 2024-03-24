import sys
from collections import deque

#정점, 간선수, 시작점
n, m, v = map(int, sys.stdin.readline().split())
graph =[[False] * (n+1) for _ in range(n+1)]

#연결된 정점을 입력
for i in range(m) :
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

def dfs(v):
    dfs_visited[v] = True 
    print(v, end=" ") # 방문 후, 정점 출력
    for i in range(1, n + 1):
        if not dfs_visited[i] and graph[v][i] == 1:  # 방문 기록이 없고, 인덱스에 값이 있다면 (연결되어 있다면)
            dfs(i) # 방문, 재귀
 
def bfs(v):
    q = deque([v])
    bfs_visited[v] = True
    while q:    
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n + 1): # 방문 기록이 없고, 인덱스에 값이 있다면 (연결되어 있다면)
            if not bfs_visited[i] and graph[v][i] == 1:
                q.append(i) # 큐에 추가
                bfs_visited[i] = True

dfs(v)
print()
bfs(v)