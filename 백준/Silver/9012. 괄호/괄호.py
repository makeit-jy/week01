import sys

def is_empty(stack):
    return not stack

cnt = int(sys.stdin.readline())

for i in range(cnt):
    ps = sys.stdin.readline().strip()
    stack = []
    flag = False

    for j in range(len(ps)) :
      if ps[j] == '(':
          stack.append(1)
      elif ps[j] == ')':
          if not is_empty(stack) : # 비어있지 않으면
            stack.pop()
          else :
            print('NO')
            flag = True
            break

    if flag :
        continue
    
    if is_empty(stack) : # 비어있으면
      print('YES')
    else :
      print('NO')