N, M = map(int, input().split())
tree_height = list(map(int, input().split()))
start, end = 1, max(tree_height)

while start <= end:
    mid = (start+end) // 2
    
    part = 0 # 벌목된 나무 총합
    for i in tree_height:
        if i >= mid:
            part += i - mid
    
    # 벌목 높이를 이분탐색
    if part >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)