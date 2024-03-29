import sys

n = int(sys.stdin.readline())
up = list(map(int, sys.stdin.readline().split()))

d = [1] * n

for i in range(1, n):
    for j in range(i):
        if up[j] < up[i]: # 부분적으로 증가하면
            d[i] = max(d[i], d[j] + 1) # i에서의 최적의 해를 갱신

print(max(d))