import sys

n, k = map(int, sys.stdin.readline().split())
pairs = [[0,0]]
DP = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    pairs.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w,v = pairs[i]
        if j >= w:
            DP[i][j] = max(DP[i-1][j] , DP[i-1][j-w] + v)
        else:
            DP[i][j] = DP[i-1][j]

print(DP[i][k])