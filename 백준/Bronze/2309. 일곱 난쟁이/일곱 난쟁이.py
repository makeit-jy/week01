seven_dwarfs = [int(input()) for _ in range(9)]
temp_list= [] # 7명을 뽑을 리스트

def dfs(depth, start):
    if depth == 7:  # 재귀를 7번 돌았다면
        if sum(temp_list) == 100:  # 일곱난쟁이들의 합이 100이라면
            for j in sorted(temp_list):  # 오름차순 정렬 후 출력
                print(j)
            exit()
        else:
            return

    for i in range(start, len(seven_dwarfs)):  # 총 9번
        temp_list.append(seven_dwarfs[i])  # 난쟁이 한 명 추가
        dfs(depth + 1, i + 1) 
        temp_list.pop() # 난쟁이 한 명 삭제

dfs(0, 0)