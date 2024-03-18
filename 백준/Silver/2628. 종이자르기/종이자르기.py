col, row = map(int, input().split())
rows = [0, row]
cols = [0, col]

cnt = int(input())

for i in range(cnt):
    who, num = map(int, (input()).split())    
    if who:
        cols.append(num)
    else:
        rows.append(num)

rows.sort()
cols.sort()
answer = 0

for i in range(len(rows) - 1):
    for j in range(len(cols) - 1):
        answer = max(answer, (cols[j + 1] - cols[j]) * (rows[i+1] - rows[i]))

print(answer)