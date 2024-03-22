import sys

cnt = int(sys.stdin.readline())
tower_list = list(map(int, sys.stdin.readline().split()))
stack = []
laser = [0] * cnt

for i in range(cnt):
    tower = tower_list[i]
    while stack and tower_list[stack[-1]] < tower:
        stack.pop()
    if stack:
        laser[i] = stack[-1] + 1
    stack.append(i)

print(' '.join(list(map(str, laser))))