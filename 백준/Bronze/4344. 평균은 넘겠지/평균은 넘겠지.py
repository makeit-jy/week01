cnt = int(input())

for i in range(cnt):
    std_list = list(map(int, input().split()))
    avg = sum(std_list[1:]) / std_list[0]  #(std_list[0]: 학생 수, std_list[1:] 점수)
    more_than_avg_std = 0
    for score in std_list[1:]:
        if score > avg:
            more_than_avg_std += 1
    rate = more_than_avg_std / std_list[0] * 100
    print(f'{rate:.3f}%')