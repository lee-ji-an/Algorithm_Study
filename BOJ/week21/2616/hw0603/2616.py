from itertools import accumulate
import sys

N = int(sys.stdin.readline())
train = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# 누적 합: 객차들 간의 승객 합을 구하기 위함
acc_train = [0] + list(accumulate(train))

# dp[i][j] : i번째 기관차까지 j번째 객차까지 고려했을 때의 최대 손님 수
dp = [[0] * (N+1) for _ in range(4)]

for i in range(1, 4):  # 기관차: i
    for j in range(i*M, N+1):  # 객차: j
        # dp[i][j-1]
        # -> j번째 객차를 선택 안 했을 때, 이전 객차까지 최대 손님 수
        # dp[i-1][j-M] + (acc_train[j] - acc_train[j-M])
        # -> j번째 객차를 선택 했을 때, 이전 소형기관차가 j-M번째 객차까지 고려했을 때의 최대 손님 수 + (j-M) ~ j번째 객차의 손님 수
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-M] + (acc_train[j] - acc_train[j-M]))

print(dp[-1][-1])
