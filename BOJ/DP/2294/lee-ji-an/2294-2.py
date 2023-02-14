import sys

input = sys.stdin.readline
N, K = map(int, input().split())

coin_values = [0] * N
for i in range(N):
    coin_values[i] = int(input())


def dp(k, coin_values):
    coin_cnt = [set() for _ in range(k)]
    visited = [False] * (k + 1)
    coin_cnt[0].add(k)
    cnt = 0
    while coin_cnt[cnt]:
        for value in coin_cnt[cnt]:
            for coin in coin_values:
                if value - coin < 0:
                    continue
                if value - coin == 0:
                    return cnt + 1
                if not visited[value - coin]:
                    coin_cnt[cnt + 1].add(value - coin)
                    visited[value - coin] = True
        cnt += 1
    return -1


print(dp(K, coin_values))
