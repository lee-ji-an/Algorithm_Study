import sys
input = sys.stdin.readline
N, K = map(int, input().split())
item_list = []
dp = [[0] * (K + 1) for _ in range(N + 1)]


def solve():
    for i in range(1, N + 1):
        weight, value = map(int, input().split())
        if weight > K:
            for j in range(1, K + 1):
                dp[i][j] = dp[i - 1][j]
            continue
        for j in range(1, weight):
            dp[i][j] = dp[i - 1][j]                                  # i 번째 물건을 넣지 않음 (넣을 수가 없음)
        for j in range(weight, K + 1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)  # i 번째 물건을 넣지 않는것 / i 번째 물건을 넣는 것 둘 중 큰 값을 저장

    print(dp[N][K])


solve()
