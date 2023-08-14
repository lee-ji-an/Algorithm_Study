import sys
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M, fuel = map(int, input().split())

answer = -1
board = [[]]
passengers = [0, 0]
for n in range(N):
    board.append([0] + list(map(int, input().split())))
cur_row, cur_col = map(int, input().split())
for m in range(M):
    p = list(map(int, input().split()))
    board[p[0]][p[1]] = m + 2
    passengers.append(p)


def find_start(row, col):
    if board[row][col] >= 2:
        return board[row][col], 0

    candidate = []
    dist = 0
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    q = deque([(row, col)])
    visited[row][col] = True
    while q:
        dist += 1
        length = len(q)
        for _ in range(length):
            row, col = q.popleft()
            for d in range(4):
                mv_row, mv_col = row + dr[d], col + dc[d]
                if not(1 <= mv_row <= N) or not(1 <= mv_col <= N):
                    continue
                if visited[mv_row][mv_col] or board[mv_row][mv_col] == 1:
                    continue

                if board[mv_row][mv_col] >= 2:
                    candidate.append((mv_row, mv_col, board[mv_row][mv_col]))
                q.append((mv_row, mv_col))
                visited[mv_row][mv_col] = True
        if candidate:
            break
    else:
        return -1, -1

    ans = min(candidate)
    return ans[2], dist


def drive(start_row, start_col, passenger_num):
    dest = (passengers[passenger_num][2], passengers[passenger_num][3])
    dist = 0

    visited = [[False] * (N + 1) for _ in range(N + 1)]
    q = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    while q:
        dist += 1
        length = len(q)

        for _ in range(length):
            row, col = q.popleft()
            for d in range(4):
                mv_row, mv_col = row + dr[d], col + dc[d]
                if not (1 <= mv_row <= N) or not (1 <= mv_col <= N):
                    continue
                if visited[mv_row][mv_col] or board[mv_row][mv_col] == 1:
                    continue
                if mv_row == dest[0] and mv_col == dest[1]:
                    return dist
                q.append((mv_row, mv_col))
                visited[mv_row][mv_col] = True
    return -1


for m in range(M):
    # 가장 가까운 손님 찾기
    p_num, dist = find_start(cur_row, cur_col)
    board[passengers[p_num][0]][passengers[p_num][1]] = 0

    if dist == -1 or fuel < dist:
        break
    fuel -= dist

    # 손님 태우고 목적지까지 가기
    drive_dist = drive(passengers[p_num][0], passengers[p_num][1], p_num)
    if drive_dist == -1 or fuel - drive_dist < 0:
        break
    fuel += drive_dist

    # 현재 위치를 태운 손님의 목적지로 갱신
    cur_row, cur_col = passengers[p_num][2], passengers[p_num][3]
else:
    answer = fuel

print(answer)
