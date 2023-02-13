import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0] + [10001] * k  # dp[i]: i원을 만드는데 필요한 동전의 최소 개수

for won in range(1, k+1):  # 1원부터 K원까지
    for coin in coins:  # 사용할 수 있는 동전들에 대하여
        if (won - coin >= 0):  # 해당 동전을 사용할 수 있는 경우
            dp[won] = min(dp[won], dp[won-coin] + 1)  # 최솟값 갱신

print(-1 if dp[k] == 10001 else dp[k])
