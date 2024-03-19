def backtracking(row, columns, col_diag, anti_diag):
    global result
    if row == N:
        result += 1
        return
    for col in range(N):
        # 현재 열(col)에 퀸이 있거나, 대각선에 퀸이 있는 경우 건너뛰기
        if columns[col] or col_diag[row + col] or anti_diag[row - col]:
            continue
        # 현재 위치에 퀸 배치
        columns[col] = True
        col_diag[row + col] = True
        anti_diag[row - col] = True
        # 다음 행으로 재귀적으로 이동
        backtracking(row + 1, columns, col_diag, anti_diag)
        # 백트래킹을 위해 퀸을 제거
        columns[col] = False
        col_diag[row + col] = False
        anti_diag[row - col] = False

N = int(input())
columns = [False] * N  # 현재 열에 퀸 존재 여부 확인 배열
col_diag = [False] * (2 * N - 1)  # / 에 퀸 존재 여부 확인 배열
anti_diag = [False] * (2 * N - 1)  # \ 에 퀸 존재 여부 확인 배열
result = 0
backtracking(0, columns, col_diag, anti_diag)
print(result)
