import sys

input = sys.stdin.readline
N, K = map(int, input().split())

coin_values = [0] * N
for i in range(N):
    coin_values[i] = int(input())


def dp(k, coin_values):
    coin_cnt = [float('inf')] * (k + 1)
    coin_cnt[k] = 0
    for i in range(k, -1, -1):
        if coin_cnt[i] >= 0:
            for coin in coin_values:
                if i - coin < 0 or coin_cnt[i - coin] <= coin_cnt[i] + 1:
                    continue
                coin_cnt[i - coin] = coin_cnt[i] + 1

    if coin_cnt[0] == float('inf'):
        return -1

    return coin_cnt[0]


print(dp(K, coin_values))
