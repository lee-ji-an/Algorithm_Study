import sys

N = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# dp[i][j] = i번 집을 j색으로 칠했을 때, 첫 집부터 i번째 집을 칠하는 데 드는 최소 비용
dp = [[sys.maxsize] * 3 for _ in range(N)]

minCost = sys.maxsize
for startColor in range(3):  # 첫 집의 색깔이 될 수 있는 R, G, B에 대해 각각 조사
    dp[0] = [sys.maxsize] * 3  # 각 경우에 대해 기본값 초기화
    dp[0][startColor] = cost[0][startColor]

    for house in range(1, N):
        # R:(GB), G:(RB), B:(RG). RGB 각 색으로 칠할 때 이전 집의 색이 될 수 있는 후보군
        for cur_color, (cand1, cand2) in enumerate(((1, 2), (0, 2), (0, 1))):
            # 현재 집을 칠하는 데 드는 비용 + 이때까지의 최솟값
            dp[house][cur_color] = cost[house][cur_color] + min(dp[house-1][cand1], dp[house-1][cand2])

    for lastColor in range(3):
        if (startColor != lastColor):  # 첫 집의 색깔과 다른 경우에만 최솟값 갱신
            minCost = min(minCost, dp[N - 1][lastColor])

print(minCost)
