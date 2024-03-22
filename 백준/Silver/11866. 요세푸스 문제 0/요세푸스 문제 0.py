from sys import stdin

N, K = map(int,stdin.readline().split())
idx = 0
queue = list(range(1, N+1))
result = []

while len(queue) > 0:
    idx += (K-1)
    idx = idx % len(queue)
    result.append(queue.pop(idx))
    
print("<",end="")
for i in range(N-1):
    print(result[i],end=", ")
print(result[N-1], end = ">")