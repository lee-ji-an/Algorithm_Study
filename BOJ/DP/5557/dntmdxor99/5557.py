n = k = int(input()) - 1
maps = [m for m in map(int, input().split())]
try:
    ans = maps.pop()
    factor = 1 if maps[0] else 0.5      # 0이 있으면 그냥 빼고 2배수 해도 됨
    while 0 in maps:        # 0을 제거하고, factor를 2씩 곱함
        maps.remove(0)
        factor *= 2
        n -= 1
    dp = [[0] * n for _ in range(21)]     # dp[가능한 숫자][현재까지 수행 횟수]
    dp[maps[0]][0] = 1
    for i in range(1, n):       # 현재 수행 횟수
        for j in range(21):     # 가능한 숫자
            if temp := dp[j][i - 1]:
                if (cur := j - maps[i]) >= 0:
                    dp[cur][i] += dp[j][i - 1]
                if (cur := j + maps[i]) <= 20:
                    dp[cur][i] += dp[j][i - 1]
    print(dp[ans][n - 1] * int(factor))
except:     # 인자가 모두 0일때는 오류가 발생함
    print(2 ** (k - 1))