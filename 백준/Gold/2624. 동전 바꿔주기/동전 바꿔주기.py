import sys

t = int(sys.stdin.readline())
k = int(sys.stdin.readline())
dp = [0]*(t+1)
dp[0] = 1

for _ in range(k):
    penny, penny_cnt = map(int, sys.stdin.readline().split())
    
    for i in range(t, -1, -1):
        j = 1
        while j <= penny_cnt and i-(penny*j) >= 0:
            dp[i] += dp[i-(penny*j)]
            j+=1
print(dp[t])