import sys
input = sys.stdin.readline

direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
N, M = map(int, input().split())
board = []
visited = [[0] * M for _ in range(N)]
for i in range(N):
    board.append(input().rstrip())


def move(row, col, cur_num):
    r, c = row, col
    while True:
        if not(0 <= r < N) or not(0 <= c < M):  # case 1 : 범위를 벗어나는 경우
            return 1
        if visited[r][c] == cur_num:  # case 2 : 내가 지나온 경로를 다시 만나는 경우
            return 1
        elif 0 < visited[r][c] < cur_num:  # case 3 : 내가 지나온 경로가 아닌 경로를 다시 만나는 경우
            return 0

        visited[r][c] = cur_num
        d = board[r][c]

        r, c = r + direction[d][0], c + direction[d][1]


num = 0
cnt = 0
for row in range(N):
    for col in range(M):
        if visited[row][col] > 0:
            continue
        num += 1
        cnt += move(row, col, num)

print(cnt)
