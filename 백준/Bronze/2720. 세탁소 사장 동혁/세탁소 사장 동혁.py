import sys

changes = [25, 10, 5, 1]
T = int(sys.stdin.readline())

for _ in range(T) :
    C = int(sys.stdin.readline())
    result = []

    for i in changes :
        result.append(C // i)
        C = C % i
        
    print(*result)
