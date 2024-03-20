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


# [20, 7, 23, 19, 10, 15, 25, 8, 13]
# before = [20]
# before = [20, 7]
# before = [20, 7, 23]
# before = [20, 7, 23, 19]
# before = [20, 7, 23, 19, 10]
# before = [20, 7, 23, 19, 10, 15]
# before = [20, 7, 23, 19, 10, 15, 25]
# after =  [20, 7, 23, 19, 10, 15]
# before = [20, 7, 23, 19, 10, 15, 8]
# after =  [20, 7, 23, 19, 10, 15]
# before = [20, 7, 23, 19, 10, 15, 13]
# after =  [20, 7, 23, 19, 10, 15]
# after =  [20, 7, 23, 19, 10]
# before = [20, 7, 23, 19, 10, 25]
# before = [20, 7, 23, 19, 10, 25, 8]
# after =  [20, 7, 23, 19, 10, 25]
# before = [20, 7, 23, 19, 10, 25, 13]
# after =  [20, 7, 23, 19, 10, 25]
# after =  [20, 7, 23, 19, 10]
# before = [20, 7, 23, 19, 10, 8]
# before = [20, 7, 23, 19, 10, 8, 13]
# 7
# 8
# 10
# 13
# 19
# 20
# 23

# seven_dwarfs = [int(input()) for _ in range(9)]
# temp_list= [] # 7명을 뽑을 리스트
# print(seven_dwarfs)

# def dfs(depth, start):
#     if depth == 7:  # 재귀를 7번 돌았다면
#         if sum(temp_list) == 100:  # 일곱난쟁이들의 합이 100이라면
#             for j in sorted(temp_list):  # 오름차순 정렬 후 출력
#                 print(j)
#             exit()
#         else:
#             return

#     for i in range(start, len(seven_dwarfs)):  # 총 9번
#         temp_list.append(seven_dwarfs[i])  # 난쟁이 한명을 추가
#         # print("before =", temp_list)

#         dfs(depth + 1, i + 1)  # dfs를 돈다(다음번 깊이는 +1로 해주고 인덱스는 중복되지 않게 하기위해서 다음 인덱스를 넣어준다.)
#         temp_list.pop()  # dfs를 돌다 7명이 다 찼으나 합이 100이 아니어서 return 되었으면 넣었던 난쟁이 한명을 다시 빼준다.
#         # print("after = ", temp_list)

# dfs(0, 0)
