import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# dp[i][j] = arr[i]까지 조사했을 때, j를 만들 수 있는 경우의 수
dp = [[0] * 21 for _ in range(N)]
dp[0][arr[0]] = 1  # 첫 번째 오는 수는 반드시 포함

# 루프 안에서 다음 숫자를 더하거나/뺐을 때의 결과가 범위 안에 있을 때만 이전 dp값을 더해 줌
for i in range(1, N-1):
    for j in range(21):
        if (dp[i-1][j]):
            for nextNum in (j+arr[i], j-arr[i]):  # 더하거나 뺐을 때
                if (0 <= nextNum <= 20):  # 상근이가 배운 숫자 범위 안이라면
                    dp[i][nextNum] += dp[i-1][j]  # 이전 dp값을 누적해 줌

print(dp[-2][arr[-1]])  # 마지막 숫자를 만들 수 있는 경우의 수 출력
