def dfs(depth):
    if depth == k:
        num_set.add(''.join(map(str, num_list)))
        return
    for i in range(n):
        if check[i]:
            continue
        num_list.append(nums[i])
        check[i] = 1
        dfs(depth+1)
        num_list.pop()
        check[i] = 0
        
n, k = int(input()), int(input())
nums = [int(input()) for _ in range(n)]
num_list, num_set = [], set()
check = [0]*n
dfs(0)
print(len(num_set))