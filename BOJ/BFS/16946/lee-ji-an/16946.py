import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
WALL, EMPTY = 1, 0
board = []
ans = [[EMPTY] * M for _ in range(N)]
walls = set()
cntDict = {}
dx = (0, 0, -1, 1)  # 상하좌우
dy = (-1, 1, 0, 0)
for i in range(N):
    board.append(list(map(int, input().rstrip())))

# 맵에 공간번호를 부여하고 면적을 return 하는 함수
def bfs(row, col, areaNum):
    q = deque()
    q.append((row, col))
    cnt = 1
    visited[row][col] = True
    board[row][col] = areaNum
    while q:
        y, x = q.popleft()
        for i in range(4):
            movex = x + dx[i]
            movey = y + dy[i]
            if movex < 0 or movex >= M or movey < 0 or movey >= N:
                continue
            if board[movey][movex] == EMPTY and not visited[movey][movex]:
                visited[movey][movex] = True
                q.append((movey, movex))
                board[movey][movex] = areaNum
                cnt += 1
    return cnt

# 벽을 부쉈을 때 이동할 수 있는 면적을 return 하는 함수
def area(row, col):
    y, x = row, col
    check = set()
    cnt = 0
    for i in range(4):
        movex = x + dx[i]
        movey = y + dy[i]
        if movex < 0 or movex >= M or movey < 0 or movey >= N:
            continue
        areaNum = board[movey][movex]
        if areaNum >= 2 and areaNum not in check:
            check.add(areaNum)
            cnt += cntDict[board[movey][movex]]
    return cnt + 1


visited = [[False] * M for _ in range(N)]
areaNum = 2
for i in range(N):
    for j in range(M):
        if board[i][j] == EMPTY and not visited[i][j]:  # 빈 공간을 발견하면 bfs 탐색
            cntDict[areaNum] = bfs(i, j, areaNum)       # 함수의 return 값(i, j 위치에서 도달할 수 있는 면적) 을 딕셔너리에 저장
            areaNum += 1
for i in range(N):
    for j in range(M):
        if board[i][j] > 1:  # 1보다 크다는 것은 공간 번호가 부여됐다는 것이므로 빈공간 -> 0출력
            print(0, end="")
        else:
            print(area(i, j) % 10, end="")  # 벽일때는 area 함수의 return 값
    print()
