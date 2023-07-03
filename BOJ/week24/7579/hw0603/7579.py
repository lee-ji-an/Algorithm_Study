from bisect import bisect_left
import sys

N, M = map(int, sys.stdin.readline().split())
memory = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(sum(cost)+1)] for _ in range(N+1)]  # dp[i][j]: i번째 앱까지 조사했을 때 j비용으로 확보할 수 있는 최대 메모리

for i in range(1, N+1):  # 앱
    for j in range(1, sum(cost)+1):  # 비용
        # 현재 앱을 끄는 비용이 j보다 크면 끌 수 없으므로 이전 앱까지의 최대 메모리를 그대로 가져옴
        if (j < cost[i]):
            dp[i][j] = dp[i-1][j]
        # 현재 앱을 끌 수 있으면 이전 앱까지의 최대 메모리와 현재 앱을 끈 후의 최대 메모리 중 큰 값을 가져옴
        else:
            dp[i][j] = max(memory[i] + dp[i-1][j-cost[i]], dp[i-1][j])

# dp[N]에서 M보다 큰 값이 처음 나오는 인덱스 출력
print(bisect_left(dp[N], M))
