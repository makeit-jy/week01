import sys 
cnt = int(sys.stdin.readline())

stack = [0]

for i in range(cnt):
    n = int(sys.stdin.readline())
    if n == 0 :
        stack.pop()
    else :
        stack.append(n)

print(sum(stack))