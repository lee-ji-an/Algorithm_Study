import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
dp = [float('inf')] * 100001

for coin in coins:
    dp[coin] = 1

# 고려하는 동전의 개수를 늘려간다
for coin in coins:
    # k까지의 모든 금액에 대해서 탐색
    for i in range(1, k+1):
        # 금액 - 동전이 0보다 작으면, 예를들어 동전이 5인데 i가 1, 2, 3, 4이라면 이전 dp에서 5를 더하는 방식으로 구할 수 없으므로 continue
        if i - coin < 0:
            continue
        # 개수의 최솟값을 갱신해준다
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != float('inf') else -1)