from collections import deque
import sys

dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

N = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[set() for _ in range(N)] for _ in range(N)]  # 0: 미방문, 1: 가로, 2: 세로 (중심점 기준) -> 2차원으로 해야함

# 초기 통나무 위치와 도착점 위치 구함
srcPos, dstPos = [], []
for i in range(N):
    for j in range(N):
        if not ((val := matrix[i][j]).isdigit()):
            (srcPos if val == 'B' else dstPos).append((i, j))

srcState = (*srcPos[1], 1 if srcPos[0][0] == srcPos[1][0] else 2)
dstState = (*dstPos[1], 1 if dstPos[0][0] == dstPos[1][0] else 2)

# print(srcState, dstState)

def print_result(movecnt):
    sys.exit(print(movecnt))

# BFS
q = deque([(*srcState,)])  # (row, col, 가로/세로)
visited[srcState[0]][srcState[1]].add(srcState[2])

moveCnt = 0
while (q):
    for _ in range(len(q)):
        row, col, state = q.popleft()

        # 상하좌우 이동 처리
        for i in range(4):
            nr, nc = row+dr[i], col+dc[i]

            # 범위 밖으로 벗어나는 경우, 벌목이 안된 경우 Skip
            if (state == 2):  # 세로
                if not (1 <= nr < N-1 and 0 <= nc < N):
                    continue
                if (any(i == '1' for i in (matrix[nr-1][nc], matrix[nr][nc], matrix[nr+1][nc]))):
                    continue
            if (state == 1):  # 가로
                if not (0 <= nr < N and 1 <= nc < N-1):
                    continue
                if (any(i == '1' for i in (matrix[nr][nc-1], matrix[nr][nc], matrix[nr][nc+1]))):
                    continue
            
            # 같은 상태로 이전에 방문한 경우 Skip
            if (state in visited[nr][nc]):
                continue

            # 종료조건
            if ((nr, nc, state) == dstState):
                print_result(moveCnt+1)
            
            visited[nr][nc].add(state)
            q.append((nr, nc, state))
        
        # 회전 처리
        if not (1 <= row < N-1 and 1 <= col < N-1):
            continue
        canRotate = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (matrix[row+i][col+j] == '1'):
                    canRotate = False

        if not (canRotate):
            continue

        newstate = 1 if state == 2 else 2
        if (newstate in visited[row][col]):
            continue

        # 종료조건
        if ((row, col, state) == dstState):
            print_result(moveCnt+1)
        visited[row][col].add(state)
        q.append((row, col, newstate))

    moveCnt += 1

print(0)
