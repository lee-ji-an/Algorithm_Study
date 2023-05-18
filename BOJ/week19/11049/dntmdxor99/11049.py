import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    maps = [[]] * n
    dp = [[float('inf')] * n for _ in range(n)]     # 최솟값을 구하기 위해 최댓값을 미리 넣어놓음

    for i in range(n):
        maps[i] = list(map(int, input().split()))

    for i in range(n):
        dp[i][i] = 0        # 대각선은 0으로 처리해놓음

    for dia in range(1, n):
        for i in range(n - dia):
            for k in range(i, i + dia):
                # i ~ i + dia까지 최적은 i ~ k, k + 1 ~ dia 까지 계산하면 됨
                # 여기서 최솟값을 찾으면 해결할 수 있음
                temp = maps[i][0] * maps[k][1] * maps[i + dia][1]
                dp[i][i + dia] = min(dp[i][i + dia], dp[i][k] + dp[k + 1][i + dia] + temp)

    print(dp[0][n - 1])
