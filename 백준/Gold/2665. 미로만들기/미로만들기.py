import sys
from collections import deque
INF = sys.maxsize

n = int(sys.stdin.readline().rstrip())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
weight = [[INF] * n for _ in range(n)]
weight[0][0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(node):
    queue = deque([node])
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if (0 <= next_x < n) and (0 <= next_y < n): # 예외처리
                if weight[next_x][next_y] > weight[cur_x][cur_y]:
                    if not maze[next_x][next_y]: # 벽이면 / # 다음에 이동할 칸이 벽이 아닌 경우
                        weight[next_x][next_y] = weight[cur_x][cur_y] + 1 
                        # 현재까지의 경로 길이(weight[cur_x][cur_y])에서 1만큼 더한 값을 다음 칸까지의 최단 경로로 설정
                    else: # 방이면
                        weight[next_x][next_y] = weight[cur_x][cur_y]
                    queue.append((next_x, next_y))

bfs((0, 0))
print(weight[n-1][n-1])