import sys

n=int(sys.stdin.readline()) # 컴퓨터 개수
v=int(sys.stdin.readline()) # 간선 개수

graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
for i in range(v): # 그래프 생성
    a, b = map(int, sys.stdin.readline().split())

    graph[a] += [b] # a 에 b 연결
    graph[b] += [a] # b 에 a 연결

def dfs(v):
    visited[v] =1 
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
dfs(1)
print(sum(visited)-1)