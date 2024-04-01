import sys, heapq

homework_cnt = int(sys.stdin.readline())
award_list = [list(map(int, sys.stdin.readline().split())) for _ in range(homework_cnt)]
award_list.sort()
result = []

for deadline, noodle in award_list:
    if deadline == len(result):
        if noodle <= result[0]:
            continue
        heapq.heappop(result)
    heapq.heappush(result, noodle)    
print(sum(result))