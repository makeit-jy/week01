import sys

meeting_cnt = int(sys.stdin.readline().strip())
meetings = []

for i in range(meeting_cnt):
    start, end = map(int, sys.stdin.readline().split(" "))
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0])) # 정렬 기준을 튜플의 두 번째 요소로 설정 (종료 시간을 오름차순 정렬하고, 시작 시간을 오름차순 정렬)

end_time = 0
max_meetings_cnt = 0
for meeting in meetings:
    if end_time <= meeting[0]:
        end_time = meeting[1]
        max_meetings_cnt += 1

print(max_meetings_cnt)