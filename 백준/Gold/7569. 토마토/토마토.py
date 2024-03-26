from sys import stdin
from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

queue = deque([])

def bfs():
	while queue:
		x, y, z = queue.popleft()
		for i in range(6):
			nx = x + dx[i]
			ny = y + dy[i]
			nz = z + dz[i]
			if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not graph[nx][ny][nz]: 
				# 토마토 상자의 범위 내에 위치하는지 확인 & 해당 위치에 있는 토마토가 아직 익지 않았는지를 확인
				graph[nx][ny][nz] = graph[x][y][z] + 1
				queue.append([nx, ny, nz])

m, n, h = map(int, stdin.readline().split())
graph = [[list(map(int, stdin.readline().split())) for _ in range(n)] for _ in range(h)]

for i in range(h):
	for j in range(n):
		for k in range(m):
			if graph[i][j][k] == 1:
				queue.append([i, j, k])
bfs()

day = 0
for i in graph:
	for j in i:
		if 0 in j:
			print(-1) # 익지 않은 토마토가 있는 경우
			exit(0)
		day = max(day, max(j))
print(day - 1) # 최대값을 찾아서 그 값에서 1을 뺀 결과를 출력 (시작이 1이어서)