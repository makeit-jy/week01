import sys 
cnt = int(sys.stdin.readline())

stack = []

for _ in range(cnt):
    word = sys.stdin.readline().split() 
    if word[0] == 'push':
        stack.append(word[1])
    elif word[0] == 'pop':
        if len(stack)>0: print(stack.pop())
        else: print(-1)
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        if len(stack)==0: print(1)
        else: print(0)
    elif word[0] == 'top':
        if len(stack)>0: print(stack[-1])
        else: print(-1)

# cnt = int(input())
# stack = []

# for _ in range(cnt):
#     word = input().split()
#     if word[0] == 'push':
#         stack.append(word[1])
#     elif word[0] == 'pop':
#         if len(stack) > 0: 
#             print(stack.pop())
#         else: print(-1)
#     elif word[0] == 'size':
#         print(len(stack))
#     elif word[0] == 'empty':
#         if len(stack)==0: 
#             print(1)
#         else: print(0)
#     elif word[0] == 'top':
#         if len(stack)>0:
#             print(stack[-1])
#         else: print(-1)