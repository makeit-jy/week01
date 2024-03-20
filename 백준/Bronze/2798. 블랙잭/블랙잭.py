import sys

n, m = map(int, sys.stdin.readline().split())
max_value = 0
card = list(map(int, sys.stdin.readline().split()))
for i in range(n - 2):
	for j in range(i + 1, n - 1):
		for k in range(j + 1, n):
			if (card[i] + card[j] + card[k] <= m):
				max_value = max(max_value, card[i] + card[j] + card[k])
print (max_value)