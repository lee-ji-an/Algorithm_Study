import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
board = [[0] * N for _ in range(N)]
fishes = {}
sy, sx = 0, 0
ssize = 2
fishCnt = 2

dx = (0, -1, 1, 0)  # 상 좌 우 하
dy = (-1, 0, 0, 1)
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            sy, sx = i, j
            board[i][j] = 0
            continue
        elif row[j] > 0:                # fishes 딕셔너리에 key : 물고기 크기, value : 물고기 갯수 를 저장해놓음
            if row[j] in fishes:
                fishes[row[j]] += 1
            else:
                fishes[row[j]] = 1
        board[i][j] = row[j]


def bfs(sy, sx, ssize, total):
    q = deque()
    minCnt = float('inf')
    myFish = []
    visited = [[False] * N for _ in range(N)]
    q.append((sy, sx, total))
    visited[sy][sx] = True
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            movey = y + dy[i]
            movex = x + dx[i]
            if movey < 0 or movey >= N or movex < 0 or movex >= N:
                continue
            if visited[movey][movex]:
                continue
            if board[movey][movex] <= ssize:                    # 지나갈 수 있는지 확인
                visited[movey][movex] = True
                if minCnt >= cnt + 1:
                    if 0 < board[movey][movex] < ssize:         # 먹을 수 있는 물고기인지 검사
                        minCnt = cnt + 1                        # 먹을 수 있는 물고기까지의 거리를 minCnt 에 저장 (다음에 이 거리보다 멀리 있는 물고기는 검사하지 않음)
                        myFish.append((movey, movex, cnt+1))    # myFish 리스트에 먹을 수 있는 물고기의 좌표를 저장
                    else:
                        q.append((movey, movex, cnt+1))
    if myFish:  # 제일 위, 왼쪽에 있는 물고기를 반환
        myFish.sort()
        return myFish[0][0], myFish[0][1], myFish[0][2]
    else:       # 먹을 수 있는 물고기는 있으나 갈 수 있는 경로가 없는 경우
        return -1, -1, total


total = 0
while True:
    flag = False
    for i in range(ssize):
        if i in fishes and fishes[i] > 0:
            sy, sx, total = bfs(sy, sx, ssize, total)   # 상어 크기보다 작은 물고기가 있으면 bfs 함수 호출 return 먹은 물고기의 좌표, 이동한 전체 거리
            if sy != -1:        # 물고기를 먹었을 때
                fishes[board[sy][sx]] -= 1
                board[sy][sx] = 0
                flag = True     # 물고기를 먹었다는 표시
                fishCnt -= 1
                if fishCnt == 0:    # 자신의 크기만큼 물고기를 먹었으면 size 증가시켜줌
                    ssize += 1
                    fishCnt = ssize
            break
    if not flag:   # 물고기를 먹지 못했으면 지금까지의 전체 거리를 print
        print(total)
        break