input_month, input_date = map(int, input().split(' '))
year_list = [31,28,31,30,31,30,31,31,30,31,30,31]
day_list = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
sum_date = 0

for i in range (input_month-1):
  sum_date += year_list[i]
date = sum_date + input_date
print(day_list[(date % 7)])