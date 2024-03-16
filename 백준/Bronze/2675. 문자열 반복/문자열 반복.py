cnt = int(input())
for i in range(cnt):
  R, S = input().split()
  for i in range(len(S)):
    print(int(R) * S[i], end='') # 개수*문자열의 인덱스. end의 역할은 공백 없애기.
  print()