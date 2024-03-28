import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    # memoization을 위한 리스트 선언
    d = [0]*(m+1)
    d[0] = 1

    for coin in coins:
        for i in range(m+1):
            if i >= coin:
                d[i] += d[i-coin]

    print(d[m])