import sys
input = sys.stdin.readline
N, S, M = map(int, input().split())
volume_list = list(map(int, input().split()))


def solve(N, S, M):
    dp = [[False] * (M + 1) for _ in range(N + 1)]
    dp[0][S] = True
    for i in range(1, N + 1):
        volume_range = volume_list[i - 1]
        for j in range(0, M + 1):
            if dp[i - 1][j]:
                if j + volume_range <= M:             # i 번째 곡에서 연주할 수 있는 볼륨을 True로 변경
                    dp[i][j + volume_range] = True
                if j - volume_range >= 0:
                    dp[i][j - volume_range] = True

    noAnswerFlag = True
    for i in range(M, -1, -1):
        if dp[N][i]:
            noAnswerFlag = False
            print(i)
            break
    if noAnswerFlag:
        print(-1)


solve(N, S, M)
