import sys

kind, value = map(int, sys.stdin.readline().split())
coin_list = []
for _ in range(0, kind):
    coin_list.append(int(sys.stdin.readline()))

dp = [0] * (value+1)
dp[0] = 1

for coin in coin_list:
    for i in range(coin, value+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[value])