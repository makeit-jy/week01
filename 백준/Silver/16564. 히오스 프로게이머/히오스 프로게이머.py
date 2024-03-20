import sys
input=sys.stdin.readline

N,K = map(int,input().split()) # 캐릭터수 N과 올릴 수 있는 레벨 K
level_list = [int(input()) for _ in range(N)] # 캐릭터별 레벨 리스트
 
low, high = min(level_list), max(level_list) + K # 캐릭터중 제일 낮은 레벨 ~ 높은 레벨 + K 까지 이분탐색
while low <= high:
    target_level = (low+high) // 2 # 팀의 목표 레벨
    need_level = sum([target_level-lv for lv in level_list if target_level-lv >= 0]) # 필요한 레벨
    
    if need_level <= K: # 필요한 레벨보다 올릴 수 있는 레벨(K)이 크거나 같은 경우
        result = target_level # result를 갱신
        low = target_level + 1
    elif need_level > K: # 필요한 레벨보다 올릴 수 있는 레벨(K)이 작은 경우
        high = target_level - 1
 
print(result)