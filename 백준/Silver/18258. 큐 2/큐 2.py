import sys
from collections import deque

cnt = int(sys.stdin.readline())
queue = deque([])

for i in range(cnt):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        queue.append(com[1])
    elif com[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif com[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])


# 시간 초과

# import sys
# cnt = int(sys.stdin.readline())
# queue = []

# for i in range(cnt):
#     command = sys.stdin.readline().split()
#     if command[0] == 'push':
#         queue.append(command[1])
#     elif command[0] == 'pop':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue.pop(0))  
#     elif command[0] == 'size':
#         print(len(queue))
#     elif command[0] == 'empty':
#         if len(queue) == 0:
#             print(1)
#         else:
#             print(0)
#     elif command[0] == 'front':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[0])
#     elif command[0] == 'back':
#         if len(queue) == 0:
#             print(-1)
#         else:
#             print(queue[-1])