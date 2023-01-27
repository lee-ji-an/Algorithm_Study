import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
starty, startx, endy, endx = map(int, input().split())
visitedS = [[-1] * N for _ in range(N)]
visitedE = [[-1] * N for _ in range(N)]
START, END = 1, 2  #시작말, 도착말을 나타냄
dx = (-1, 1, -2, 2, -1, 1)
dy = (-2, -2, 0, 0, 2, 2)

def msbfs():
    q = deque()
    q.append((starty, startx, 0, START))
    visitedS[starty][startx] = 0
    q.append((endy, endx, 0, END))
    visitedE[endy][endx] = 0
    while q:
        y, x, cnt, check = q.popleft()
        for i in range(6):
            movex = x + dx[i]
            movey = y + dy[i]
            if movey < 0 or movey >= N or movex < 0 or movex >= N:
                continue
            if check == START:
                if visitedS[movey][movex] != -1:
                    continue
                elif visitedE[movey][movex] == -1:              # END 에서 온 적이 없으면 q에 넣음
                    q.append((movey, movex, cnt + 1, START))
                    visitedS[movey][movex] = cnt + 1
                else:
                    return visitedE[movey][movex] + cnt + 1     # END 에서 방문한 적이 있으면 cnt의 합을 return
            if check == END:
                if visitedE[movey][movex] != -1:
                    continue
                elif visitedS[movey][movex] == -1:              # START 에서 온 적이 없으면 q에 넣음
                    q.append((movey, movex, cnt + 1, END))
                    visitedE[movey][movex] = cnt + 1
                else:                                           # START 에서 방문한 적이 있으면 cnt의 합을 return
                    return visitedS[movey][movex] + cnt + 1
    return -1


visited = [[False]*N for _ in range(N)]
def bfs():
    q = deque()
    q.append((starty, startx, 0))
    visited[starty][startx] = True
    while q:
        y, x, cnt = q.popleft()
        for i in range(6):
            movex = x + dx[i]
            movey = y + dy[i]
            if movey < 0 or movey >= N or movex < 0 or movex >= N:
                continue
            if movey == endy and movex == endx:  # start에서 시작해서 end에 도착
                return cnt + 1
            if not visited[movey][movex]:
                q.append((movey, movex, cnt + 1))
                visited[movey][movex] = True
    return -1
# print(msbfs())
print(bfs())