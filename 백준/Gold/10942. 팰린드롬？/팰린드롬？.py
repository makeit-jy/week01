import sys

n = int(sys.stdin.readline().strip())
palindrome_map = list(map(int, sys.stdin.readline().strip().split()))
dp = [[0]*n for i in range(n)]

for i in range(n):
    dp[i][i]=1
for i in range(n-1):
    if palindrome_map[i]==palindrome_map[i+1] : dp[i][i+1]=1
    else : dp[i][i+1]=0
for cnt in range(n-2):
    for i in range(n-2-cnt):
        j = i+2+cnt
        if palindrome_map[i]==palindrome_map[j] and dp[i+1][j-1]==1 :
            dp[i][j]=1

m = int(sys.stdin.readline().strip())
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(dp[a-1][b-1])