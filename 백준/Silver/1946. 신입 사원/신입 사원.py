import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    tobe_freshman_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    tobe_freshman_list.sort()

    cnt = 1
    ranking = tobe_freshman_list[0][1]
    for i in range(1, N):
        if ranking > tobe_freshman_list[i][1]:
            cnt += 1
            ranking = tobe_freshman_list[i][1]

    print(cnt)