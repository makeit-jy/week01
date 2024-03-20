n = int(input())
solution = list(map(int, input().split(' ')))

solution.sort()

# 투포인터 설정
left = 0
right = n-1

answer = float('inf') # 무한대를 나타내는 특수한 부동 소수점 값
final_list = [] # 정답

# 투포인터 진행
while left < right:
    s_left = solution[left]
    s_right = solution[right]

    total = s_left + s_right
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(total) < answer:
        answer = abs(total)
        final_list = [s_left, s_right]
	
    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 0에 가깝게 이동
    if total < 0:
        left += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 0에 가깝게 이동
    else:
        right -= 1

print(final_list[0], final_list[1])