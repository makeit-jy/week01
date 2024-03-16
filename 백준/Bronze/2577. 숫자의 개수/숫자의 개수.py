a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c)

for i in range(10):
  print(mul.count(str(i))) # 문자열 함수 count()를 통해 문자열 내 특정 요소의 개수 찾기