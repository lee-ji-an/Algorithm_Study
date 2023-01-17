import sys

input = sys.stdin.readline
dx = [1, 0, -1, 0]  # 우 하 좌 상
dy = [0, 1, 0, -1]
board = []
check = set()


def dfs(s, row, col):               # dfs로 특정 문자를 탐색 -> cycle이 존재하는지 확인
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(row * M + col, N * M):
        subY, subX = i // M, i % M
        if visited[subY][subX] == 0 and board[subY][subX] == s:
            stack = [0 for _ in range(N * M)]
            top = 0
            visited[subY][subX] = 1
            before = -1
            stack[top] = (subY, subX, before)
            while top != -1:
                node = stack[top]
                y, x, before = node[0], node[1], node[2]
                top -= 1
                for d in range(4):
                    movex = x + dx[d]
                    movey = y + dy[d]
                    if movex < 0 or movex > M - 1 or movey < 0 or movey > N - 1:
                        continue
                    if (before == 0 and d == 2) or (before == 2 and d == 0) or (before == 1 and d == 3) or (
                            before == 3 and d == 1):    # 내가 거쳐온 노드로 바로 돌아가는 것 방지
                        continue
                    if board[movey][movex] == s:
                        if visited[movey][movex] == 1:      # 방문한 지점 재방문하면 cycle 존재
                            return True
                        top += 1
                        stack[top] = (movey, movex, d)
                        visited[movey][movex] = 1
    return False


N, M = map(int, input().split())  # M: 가로, N: 세로
for i in range(N):
    board.append(input().strip())
for i in range(N):
    for j in range(M):
        if board[i][j] not in check:
            if dfs(board[i][j], i, j):   # board 탐색 중 내가 모르는 문자가 나오면 dfs함수 호출
                print("Yes")
                exit(0)
            else:
                check.add(board[i][j])
print("No")
