import math

def isPrime(N): # 소수 판별 함수
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

cnt = int(input())

for i in range(cnt):
    num = int(input())
    
    minus = num // 2 # 감소할 변수
    plus = num // 2 # 증가할 변수
    
    for j in range(num // 2):
        if isPrime(minus) and isPrime(plus): # 두 수가 소수이면 출력
            print(minus, plus)
            break
        else: # 소수가 아니면 1씩 증가, 감소
            minus -= 1
            plus += 1