import sys
input = sys.stdin.readline
n = int(input())
num = [0] + list(map(int, input().split()))
# dp[i][j] = i번째 숫자까지 고려하여 j를 만드는 경우의 수
dp = [[0] * 21 for _ in range(n+1)]

dp[1][num[1]] = 1

for i in range(2, n):
    for j in range(21):
        if dp[i-1][j] != 0:
            # 이전 dp값에서 num[i]를 더하고 뺀 값이 0<= <=20 범위 내에 있으면 만들 수 있다는 것이므로 dp 배열에 추가
            if 0 <= j + num[i] <= 20:
                dp[i][j + num[i]] += dp[i-1][j]
            if 0 <= j - num[i] <= 20:
                dp[i][j - num[i]] += dp[i-1][j]
                
# 마지막 수를 제외한 n-1개의 수로 마지막 수인 num[-1]을 만드는 경우의 수, 즉 dp[n-1][num[-1]] 출력
print(dp[n-1][num[-1]])