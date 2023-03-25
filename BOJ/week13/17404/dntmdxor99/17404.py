import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    dp = [[float('inf')] * 3 for _ in range(n)]
    dir = [[0, 1, 2], [1, 0, 2], [2, 0, 1]]
    mins = float('inf')

    for start in range(3):      # 시작을 달리하기 위하여
        dp[0] = [float('inf')] * 3
        dp[0][start] = maps[0][start]

        for row in range(1, n):     # 최솟값으로 갱신함
            for i, j, k in dir:
                dp[row][i] = maps[row][i] + min(dp[row - 1][j], dp[row - 1][k])

        for end in range(3):
            if start != end:        # 시작과 다를 경우에만 최솟값을 갱신함
                mins = min(mins, dp[n - 1][end])

    print(mins)
