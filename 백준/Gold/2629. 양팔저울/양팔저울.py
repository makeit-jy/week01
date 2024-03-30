import sys

n, weight_lst = int(sys.stdin.readline().strip()), list(map(int, sys.stdin.readline().split()))
m, check_weight_lst = int(sys.stdin.readline().strip()), list(map(int, sys.stdin.readline().split()))

dp = [0]
for weight in weight_lst:
    temp=[]
    for i in dp:
        temp.append(i+weight)
        temp.append(abs(i-weight))
    dp = list(set((dp + temp)))

for weight in check_weight_lst:
    print('Y' if weight in dp else 'N',end=' ')