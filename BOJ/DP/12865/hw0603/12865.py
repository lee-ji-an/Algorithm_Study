import sys

N, K = map(int, sys.stdin.readline().split())
items = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]  # dp[i][j] = i번째 물건(1-base)까지 조사했을 때, 무게 j로 얻을 수 있는 최대 가치

for i in range(1, N+1):
    for weight in range(1, K+1):  # weight: 현재 무게 제한
        if (items[i][0] > weight):  # 현재 조사하는 물건의 무게가 무게 제한값보다 크면
            dp[i][weight] = dp[i-1][weight]  # 넣지 않고 예전 dp 값 불러와서 씀
        else:  # 무게제한이 현재 물건보다 커서 적어도 현재 물건 하나는 들어갈 수 있는 경우
            # 넣지 않는 경우와 넣는 경우 둘 중 가치가 높은 경우를 택함
            dp[i][weight] = max(dp[i-1][weight], dp[i-1][weight - items[i][0]] + items[i][1])

print(dp[-1][-1])
