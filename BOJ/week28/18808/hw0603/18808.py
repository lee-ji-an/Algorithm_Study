import sys

N, M, K = map(int, sys.stdin.readline().split())
notebook = [[0]*M for _ in range(N)]

# 스티커를 붙일 수 있는지 검사
def check(row, col, R, C, lst):
    for nr in range(R):
        for nc in range(C):
            if not (0 <= row+nr < N and 0 <= col+nc < M):
                return False
            if (lst[nr][nc] & notebook[row+nr][col+nc]):
                return False
    return True

# 스티커를 붙임
def paste(row, col, R, C, lst):
    for nr in range(R):
        for nc in range(C):
            if (lst[nr][nc]):
                notebook[row+nr][col+nc] = 1

# 스티커를 시계방향으로 90도 회전
def clockwise(lst, R, C):
    tmp = [[0]*R for _ in range(C)]
    for y in range(C):
        for x in range(R):
            tmp[y][x] = lst[R-x-1][y]
    return tmp, C, R

# 확인->회전 4번 반복
def check_and_rotate(lst, R, C):
    for _ in range(4):
        for row in range(N):
            for col in range(M):
                if (check(row, col, R, C, lst)):
                    paste(row, col, R, C, lst)
                    return True
        else:
            lst, R, C = clockwise(lst, R, C)
    else:
        return False  # 스티커를 못 붙임


# 각 스티커에 대해 확인->회전 반복
for _ in range(K):
    R, C = map(int, sys.stdin.readline().split())
    lst = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(R)]
    check_and_rotate(lst, R, C)

ans = sum(notebook[i][j] for i in range(N) for j in range(M))
print(ans)
