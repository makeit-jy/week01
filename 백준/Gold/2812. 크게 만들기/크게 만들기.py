import sys

n, k = map(int, input().split(' '))
num = list(sys.stdin.readline().strip())

stack = []

for i in range(n):
    while(k > 0 and stack and stack[-1] < num[i]):
        stack.pop()
        k-=1
    stack.append(num[i])
    
stack = stack[:-k] if k > 0 else stack
# k > 0가 참(True)이면, stack[:-k]를 실행하여 stack의 마지막 k개의 요소를 제거한 새로운 리스트 생성
# k > 0가 거짓(False)이면, stack을 그대로 반환

print(''.join(stack))
