# def solve(a):
#     return sum(a) # 파이썬의 sum() 함수 이용

def solve(a):
  ans = 0
  for value in a:
    ans += value  # 리스트 a의 원소 이용
  return ans