import sys
from collections import deque

N=int(sys.stdin.readline()) # 부품 수 N 완제품
V=int(sys.stdin.readline()) # 간선 수
adj=[[] for _ in range(N+1)] #연결 정보
indegree=[0]*(N+1) # 부품별 진입차수 0일 경우 기본부품
needs=[[0]*(N+1) for _ in range(N+1)] # 각 부품이 기본부품 얼마나 필요한지

for i in range(V):
    a,b,c = map(int,sys.stdin.readline().split())
    adj[b].append([a,c])  # a 만드는데 b가 c개 필요
    indegree[a]+=1  # 진입차수

queue=deque()
basic_parts=[]
for i in range(1,N+1):
    if indegree[i]==0:
        basic_parts.append(i) #기본부품 리스트
        queue.append(i)

while queue:
    now=queue.popleft()
    for object, n in adj[now]:
        if now in basic_parts:   # 기본부품일 경우 목표 제품에 +n개
            needs[object][now]+=n
        else:
            for i in range(1,N+1):
                needs[object][i]+=needs[now][i]*n
        indegree[object]-=1
        if indegree[object]==0:
            queue.append(object)

for i in range(N+1):
    if needs[N][i] > 0:
        print(i,needs[N][i])