import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    # 파일을 합칠 때는 그 파일을 만드는 데 들었던 비용 + 두 파일의 구간 합
    # dp[i][j] = index i부터 j까지의 파일을 하나로 합치는 데 드는 최소 비용
    dp = [[0] * (n+1) for _ in range(n+1)]

    # 부분합 계산
    s = [0] * (n+1)
    for i in range(1, n+1):
        s[i] = s[i-1] + arr[i]

    # 만들 파일의 길이
    for j in range(1, n):
        # 1 ~ 1+j부터 n-j ~ n까지
        for i in range(1, n+1-j):
            '''
            ex) index 1~4를 합칠 때
            dp[1][1] + dp[2][4]
            dp[1][2] + dp[3][4]
            dp[1][3] + dp[4][4]
            중에서 최솟값과 index 1~4의 부분합 s[4]-s[0]의 합
            '''
            dp[i][i+j] = min([dp[i][i+k] + dp[i+k+1][i+j] for k in range(j)]) + (s[i+j] - s[i-1])

    # 처음부터 끝까지의 파일을 하나로 합치는 데 드는 최소 비용
    print(dp[1][n])