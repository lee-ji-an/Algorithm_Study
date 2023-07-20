import sys
input = sys.stdin.readline

N = int(input())

board = []
right_top = [False] * (N * 2 - 1)  # 존재 여부
right_down = [False] * (N * 2 - 1)
ans = 0

for i in range(N):
    board.append(list(map(int, input().split())))


def check(row, col):
    if right_down[row - col]:
        return False
    return True


def dfs(n, cnt):
    global ans
    ans = max(ans, cnt)
    start_row, end_row = (0, n + 1) if n < N else (n-N+1, N)
    flag = False
    for i in range(start_row, end_row):
        row, col = i, n - i
        if board[row][col] == 1 and check(row, col):
            flag = True
            right_down[row - col] = True
            dfs(n + 1, cnt + 1)
            right_down[row - col] = False
    # 놓을 수 있는 공간이 하나도 없을 경우
    if not flag and n <= N * 2 - 1:
        dfs(n + 1, cnt)


dfs(0, 0)
print(ans)
