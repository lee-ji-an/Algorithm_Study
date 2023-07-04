import sys
input = sys.stdin.readline

'''
필요한 메모리 바이트만큼 확보, 동시에 오버헤드는 작게
오버헤드가 0인 것을 우선적으로 확보하고 구해야 하는 답에서 뺀다
그 다음에 (오버헤드, 메모리) 순으로 정렬하여 knapsack 처럼 dp
처음으로 구해야 하는 답을 넘은 오버헤드를 찾음
'''

n, k = map(int, input().split())
m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(c) + 1)] for _ in range(n + 1)]
result = sum(c)

for i in range(1, n+1):
    byte = m[i]
    cost = c[i]

    for j in range(1, sum(c) + 1):
        if cost > j:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], byte + dp[i-1][j-cost])

        if dp[i][j] >= k:
            result = min(result, j)

if k:
    print(result)
else:
    print(0)