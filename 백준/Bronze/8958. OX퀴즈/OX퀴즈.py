# cnt = int(input())

# for i in range(cnt):
#   a = input()
#   arrow = 0
#   sum = 0
#   for j in a:
#     if j == 'O':
#         arrow += 1
#     else:
#         arrow = 0
#     sum += arrow
#   print(sum)

# 방식 1. -> 더 파이썬스럽고, 효율적
# 특징 1) 입력을 문자열 그대로 받고, 문자열의 각 문자에 직접 접근하여 처리(리스트 사용 X)
#      2) 문자열을 그대로 사용하므로 메모리 사용이 더 적을 수 있다.
#      3) 문자열에 직접 접근하기 때문에 더 빠를 수 있다.

cnt = int(input())

for i in range(cnt):
  ox_list = list(input())
  arrow = 0
  sum = 0
  for ox in ox_list:
      if ox == 'O':
          arrow += 1
          sum += arrow
      elif ox =='X':
          arrow = 0
  print(sum)

# 방식 2.
# 특징 1) 입력받은 문자열을 리스트로 변환 (각 문자에 개별적으로 접근할 수 있도록)
#      2) 입력 받은 후에 리스트로 변환하므로 메모리 사용이 더 많을 수 있다.
#      3) 리스트를 이용하여 각 문자에 하나씩 접근하고 있다.