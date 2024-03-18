# 제곱근까지만 계산하면 되는 소수의 성질 이용
# (1보다 큰 정수의 경우 자신의 제곱근보다 작은 수로 나누어지지 않는다면 소수) 

cnt = int(input())
num_list = map(int, input().split())

isPrime = False
prime_cnt = 0

for i in num_list:
  prime_friend = 0
  for j in range (2, i//2+1):
    if (i % j == 0):
      prime_friend += 1
      break
  if i!=1 and prime_friend == 0:
    prime_cnt += 1

print(prime_cnt)


# 에라토스테네스의 체

# def eratosthenes(n):
#     prime_numbers = [False, False] + [True] * (n - 1)

#     for i in range(2, n + 1):
#         if prime_numbers[i]:
#             for j in range(i * 2, n + 1, i):
#                 prime_numbers[j] = False

#     return prime_numbers

# cnt = int(input())
# num_list = map(int, input().split())

# prime_cnt = 0

# for i in num_list:
#     if eratosthenes(1001)[i]:
#         prime_cnt += 1

# print(prime_cnt)