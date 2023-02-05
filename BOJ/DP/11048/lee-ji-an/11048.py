import sys

input = sys.stdin.readline

board = []

N, M = map(int, input().split())
for _ in range(N):
    board.append(list(map(int, input().split())))


def dp():
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            candy_list[i][j] = max(candy_list[i - 1][j - 1], candy_list[i - 1][j], candy_list[i][j - 1]) + board[i - 1][j - 1]

    return candy_list[N][M]


candy_list = [[0] * (M + 1) for _ in range(N + 1)]
print(dp())
