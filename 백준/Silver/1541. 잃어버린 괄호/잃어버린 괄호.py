import sys

minus_seperated_list = sys.stdin.readline().split('-')
total_list = []

sum = 0
for i in minus_seperated_list:
    sum = 0
    plus_seperated_list = i.split('+')
    for j in plus_seperated_list:
        sum += int(j)
    total_list.append(sum)

tobe_minus = total_list[0]

for i in range(1, len(total_list)):
    tobe_minus -= total_list[i]

print(tobe_minus)