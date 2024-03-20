import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 10001

for i in range(N):
    num = int(input())
    arr[num] += 1

for j in range(1, 10001):
    if (arr[j] != 0):
        for _ in range(arr[j]):
            print(j)