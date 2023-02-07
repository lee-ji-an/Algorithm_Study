import sys


def sol():
    n = int(sys.stdin.readline().strip())
    board = list(sys.stdin.readline().split())
    m = int(sys.stdin.readline().strip())
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    for i in range(n - 1):
        dp[i][i + 1] = 1 if board[i] == board[i + 1] else 0     # i부터 i + 1번째까지

    for j in range(2, n):      # i로부터 2칸 떨어진 애들부터 봄
        for i in range(n - j):       # i부터 i + j까지 팰린드롬인지 봄, 2칸 떨어진 애들을 본다면 0~2, 1~3, 2~4가 최대 범위임
            if board[i] == board[i + j] and dp[i + 1][i + j - 1]:       # i와 i + j번째가 같고, i + 1 ~ i + j - 1이 팰린드롬이라면 i ~ i + j도 팰린드롬임
                dp[i][i + j] = 1

    for _ in range(m):
        s, e = map(int, sys.stdin.readline().split())
        print(dp[s - 1][e - 1])


sol()