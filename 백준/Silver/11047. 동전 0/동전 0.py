import sys

N, K = map(int, sys.stdin.readline().split())
money = []

for i in range(N):
  money.append(int(sys.stdin.readline().strip()))

cnt = 0
share = 0
reversed_money = reversed(money)
for i in reversed_money:  
  share = K // i
  cnt += share
  K %= i
print(cnt)