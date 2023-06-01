import sys
input = sys.stdin.readline

N = int(input())
passenger = list(map(int, input().split()))
train_len = int(input())
prefix_sum = [0] * N
dp = [[0] * N for _ in range(4)]

# 승객 수의 누적합 구하기
num = 0
for i in range(N):
    num += passenger[i]
    prefix_sum[i] = num

for i in range(1, 4):
    for j in range(train_len * i - 1, N):
        # dp[i][j] : 1 ~ i 번째 소형 기관차들이 j 까지의 범위에서 태울 수 있는 승객의 최댓값
        if j == train_len * i - 1:
            dp[i][j] = prefix_sum[j]
        else:
            dp[i][j] = max(
                dp[i][j - 1], dp[i - 1][j - train_len] + (prefix_sum[j] - prefix_sum[j - train_len])
            )

print(dp[3][N - 1])
