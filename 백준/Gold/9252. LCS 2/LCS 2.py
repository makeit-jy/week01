import sys

a = list(str(sys.stdin.readline().strip()))
b = list(str(sys.stdin.readline().strip()))

dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

# DP 테이블 채우기
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# LCS 길이 출력
print(dp[len(a)][len(b)])

# LCS 문자열 역추적
i, j = len(a), len(b)
lcs = [] 

while i > 0 and j > 0:
    if a[i-1] == b[j-1]:
        lcs.append(a[i-1])
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

# LCS 문자열이 역순으로 추적되므로, 정순으로 출력하기 위해 뒤집는다.
lcs.reverse()
print(''.join(lcs))