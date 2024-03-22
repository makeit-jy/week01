import sys

ps_list = sys.stdin.readline().rstrip()
stack = []
cnt = 1
result = 0

for i in range(len(ps_list)):
    if ps_list[i] == '(':
        stack.append(ps_list[i])
        cnt *= 2
    elif ps_list[i] == '[':
        stack.append(ps_list[i])
        cnt *= 3
    elif ps_list[i] == ')':
        if stack == [] or stack[-1] == '[':
            print(0)
            break
        else:
            if ps_list[i-1] =='(':
                result += cnt
            stack.pop()
            cnt //= 2
    elif ps_list[i] == ']':
        if stack == [] or stack[-1] == '(':
            print(0)
            break
        else:
            if ps_list[i-1] =='[':
                result += cnt
            stack.pop()
            cnt //= 3
else:
    if stack:
        print(0)
    else:
        print(result)