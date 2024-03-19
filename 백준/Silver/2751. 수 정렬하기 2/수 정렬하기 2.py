import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input().rstrip()) for _ in range(n)]

# Merge Sort
def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    
    # 배열 반으로 나누기
    mid = len(lst) // 2

    # 나뉜 배열들을 각각 정렬하기
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    # 다시 하나의 배열로 합치기
    return merge(left, right)

def merge(left, right):
    merged = []
    p1, p2 = 0, 0 # 나뉜 배열 2개를 각각 가리키는 인덱스

    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            merged.append(left[p1])
            p1 += 1
        else:
            merged.append(right[p2])
            p2 += 1
        
    # 남은 요소 추가
    merged.extend(left[p1:])
    merged.extend(right[p2:])
    
    return merged

sorted_lst = mergeSort(lst)

for num in sorted_lst:
    print(num)