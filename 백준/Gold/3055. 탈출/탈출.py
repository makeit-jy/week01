import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

visited = [[-1] * C for _ in range(R)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque()

for y in range(R):
    for x in range(C):
        if map[y][x] == '*':  # 물 좌표를 앞에 추가
            queue.appendleft((y, x))
        elif map[y][x] == 'S':  # 고슴도치는 뒤에 추가 (고슴도치는 물이 찰 예정인 칸으로 이동 불가)
            queue.append((y, x))
            visited[y][x] = 0  # 출발점에 시간 0 저장

while queue:
    y, x = queue.popleft()
    cur = map[y][x]  # 현재 위치
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]  # 이동할 좌표

        if ny < 0 or ny >= R or nx < 0 or nx >= C:  # 범위 밖이면 무시
            continue
        if visited[ny][nx] != -1:  # 이미 방문한 곳 무시
            continue
        if map[ny][nx] == "*":  # 물 무시
            continue
        if map[ny][nx] == "X":  # 돌 무시
            continue
        if cur == "*" and map[ny][nx] == "D":  # 물이 굴 가려면 무시
            continue

        if cur == "S":
            if map[ny][nx] == "D":  # 고슴도치가 가려는 위치가 굴이면 도착
                print(visited[y][x] + 1)
                break
            visited[ny][nx] = visited[y][x] + 1  # 굴 아니면 도착 시간 +1

        map[ny][nx] = cur  # 다음 좌표를 고슴도치 or 물로 변경
        queue.append((ny, nx))  # 다음 탐색 위치 추가
    else:
        continue
    break
else:
    print("KAKTUS")