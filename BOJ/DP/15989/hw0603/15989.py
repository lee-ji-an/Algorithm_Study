import sys

T = int(sys.stdin.readline())
dp = [1] * 10001  # dp[i] = 1, 2, 3으로 i를 만들 수 있는 경우의 수

for i in (2, 3):
    for j in range(i, 10000+1):
        dp[j] += dp[j-i]

# 테스트 케이스들
for _ in range(T):
    print(dp[int(sys.stdin.readline())])
