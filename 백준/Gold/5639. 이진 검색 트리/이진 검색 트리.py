import sys

sys.setrecursionlimit(10**8)

arr = []
while True:
    node = sys.stdin.readline().strip()
    if not node:  # 입력이 빈 문자열일 경우 반복문 종료
        break
    arr.append(int(node))

def post_order(start, end):
    if start > end:
        return

    s = arr[start]
    idx = end + 1
    for i in range(start+1, end+1):
        if s < arr[i]:
            idx = i
            break

    post_order(start+1, idx-1)
    post_order(idx, end)
    
    print(arr[start])

post_order(0, len(arr)-1)