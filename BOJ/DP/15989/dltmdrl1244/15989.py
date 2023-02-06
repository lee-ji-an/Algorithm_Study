import sys
input = sys.stdin.readline

dp = [[0] * 3 for _ in range(10001)]

for i in range(10001):
    # 1로 i를 만드는 경우의 수는 1개
    dp[i][0] = 1
    # 2를 추가해서 i를 만드는 경우는 '1로만 i-2를 만드는 경우의 수' + '2를 추가해서 i-2를 만드는 경우의 수'
    if i-2 >= 0:
        dp[i][1] = dp[i-2][0] + dp[i-2][1]

    # i-3번째의 경우의 수에 3을 더해서 i를 만들 수 있다
    if i-3 >= 0:
        dp[i][2] = sum(dp[i-3])

for i in range(20):
    print(i, dp[i][0], dp[i][1], dp[i][2])