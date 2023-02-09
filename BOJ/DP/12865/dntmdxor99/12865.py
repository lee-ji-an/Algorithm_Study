n, k = map(int, input().split())
board = [[b for b in map(int, input().split())] for _ in range(n)]
w, v = [0] + [a for a, b in board], [0] + [b for a, b in board]
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, k + 1):       # 현재 나는 가방에 j만큼 넣을 수 있음
        dp[i][j] = dp[i - 1][j] if w[i] > j else max(dp[i - 1][j], v[i] + dp[i - 1][j - w[i]])
        # 만약 i번째 물건의 무게가 j보다 크다면, i - 1번째 물건 가치를 넣음
        # 만약 i번째 물건의 무게가 j보다 작다면, 추가로 넣을 수 있음
        # 따라서 i번째 물건을 넣을지 말지 결정 해야함
        # i - 1번째 물건의 가치(i번째 안 넣음) vs i번째 물건의 가치 + i - 1번째에서 j - w[i] (i번째를 넣고, j - w[i]도 넣음)

        # (테케) 만약 i가 1이라면 j가 6부터 첫 번째 물건을 넣음
        # i가 2라면 j가 4일때부터 물건을 넣음, 하지만 j가 6이 되면 dp[1][6]과 8 + dp[1][6 - 6]과 비교해야 함 -> 따라서 j가 6인 순간부터는 두 번째 물건을 넣지 않음
        # i가 3이라면 j가 3일때부터 물건을 넣음, 위와 마찬가지로 쭉 최적값을 계산함
print(dp[n][k])