import sys

N, B = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def matrix_mul(arr1, arr2):
    result = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            s = sum(arr1[row][i] * arr2[i][col] for i in range(N))
            result[row][col] = s % 1000
    return result

def power(n, arr):
    if n == 1:
        return arr
    # n이 짝수일 때
    if n % 2 == 0:
        half = power(n//2, arr)  # 절반을 계산
        return matrix_mul(half, half)  # 제곱 계산
    # n이 홀수일 때
    else:
        return matrix_mul(arr, power(n-1, arr))  # n-1로 짝수로 만들어서 제곱 계산

for row in power(B, A):
    print(*[r % 1000 for r in row])