import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

def solve(cost, start):
    # 첫 번째 칸에는 start 색깔만 칠한다고 가정
    # 나머지 색깔은 비용을 1,000,001로 설정해서 칠해지는 일이 없도록 하여 dp 연산을 수행함
    dp = [[0] * 3 for _ in range(n)]
    t = cost[0][start]
    cost[0] = [1000001] * 3
    cost[0][start] = t

    dp[0] = cost[0]
    for i in range(1, n):
        for j in range(3):

            dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + cost[i][j]
    # 마지막 칸에 start 색깔이 칠해진 경우는 인정하지 않고, 비용의 합의 최솟값을 반환
    dp[-1][start] = 1000001
    return min(dp[-1])


ans = float('inf')
# 첫 번째 칸에 각각 R, G, B 색깔을 고정
for i in range(3):
    ans = min(ans, solve(cost[:], i))

print(ans)