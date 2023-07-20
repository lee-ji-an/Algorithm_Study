import sys
sys.setrecursionlimit(10**8)

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
diag_down = [False] * (2*N-1)  # 우하향 대각선 별 비숍 존재 여부

result = 0
isCollide = lambda row, col: True if diag_down[row-col] else False


def dfs(diagIdx, bishopCnt):
    global result

    # 존재하는 대각선 개수를 초과한 경우 리턴
    if (diagIdx > 2*N-1):
        return

    result = max(result, bishopCnt)
    lb, ub = (0, diagIdx+1) if diagIdx < N else (diagIdx-N+1, N)
    marked = False

    for r in range(lb, ub):
        row, col = (r, diagIdx-r)  # 우상향 대각선에 있는 칸: row+col = diagIdx

        if not (board[row][col]):  # 놓을 수 없는 칸 Skip
            continue
        if (isCollide(row, col)):  # 충돌하는 칸 Skip
            continue
        
        # 놓을 수 있고, 충돌하지 않는 칸에 대하여 비숍을 놓은 뒤 재귀호출
        diag_down[row-col] = True
        dfs(diagIdx+1, bishopCnt+1)
        diag_down[row-col] = False
        marked = True
    
    # 새 비숍을 하나도 놓지 못한 경우 다음 대각선으로 이동
    if not (marked):
        dfs(diagIdx+1, bishopCnt)


dfs(0, 0)
print(result)
