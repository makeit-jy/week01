import sys

cnt = int(sys.stdin.readline())
stack = []

for _ in range(cnt):
    stack.append(int(sys.stdin.readline()))

standard_num = stack[-1]
total = 1 # 막대기 1개는 무조건 보이니까 초기값 1

for i in reversed(range(cnt)):
    if stack[i] > standard_num:
        total += 1
        standard_num = stack[i]

print(total)