import sys

n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split())) 
arr = []
visited = [False] * n

max_ans = float('-inf')

def dfs(depth):
  global max_ans
  if depth == n:
    ans = 0
    for i in range(n-1):
      ans += abs(num_list[arr[i]] - num_list[arr[i+1]])
    max_ans = max(max_ans,ans)
    return 
  for i in range(n):
    if not visited[i]:
      visited[i] = True
      arr.append(i)
      dfs(depth + 1)
      visited[i] = False
      arr.pop()
    
dfs(0)
print(max_ans)