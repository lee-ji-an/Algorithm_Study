def solve():
    import sys
    input = sys.stdin.readline
    N = int(input())
    board = [0] + list(map(int, input().split()))
    dp = [[True] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N):                   # 이웃한 2개의 숫자끼리 검사
        if board[i] != board[i + 1]:        # i ~ j 인덱스가 palindrome 이면 dp[i][j] = True / 아니면 dp[i][j] = False
            dp[i][i + 1] = False

    for i in range(2, N):
        for j in range(1, N - i + 1):
            if not dp[j + 1][j + i - 1]:
                dp[j][j + i] = False
            elif dp[j + 1][j + i - 1]:
                if board[j] != board[j + i]:
                    dp[j][j + i] = False
    M = int(input())
    for i in range(M):
        start, end = map(int, input().split())
        print(int(dp[start][end]))


solve()
