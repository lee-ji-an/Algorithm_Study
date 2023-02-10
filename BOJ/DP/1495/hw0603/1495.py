import operator
import sys

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))

dp = [[False] * (M+1) for _ in range(N+1)]  # dp[i][vol] = 볼륨 vol이 i번째 곡(1-base)에서 가능한가?
dp[0][S] = True  # 1번째 곡 시작 전 볼륨은 S

for i in range(N):  # 곡 순회
    for vol in range(M+1):  # 0~M까지의 볼륨을 모두 테스트
        if (dp[i][vol]):  # 이번 곡을 볼륨 vol로 연주할 수 있을 경우
            # 다음 곡의 볼륨으로 가능한 값들 마킹
            if ((vol_plus := vol+V[i]) <= M):
                dp[i+1][vol_plus] = True
            if ((vol_minus := vol-V[i]) >= 0):
                dp[i+1][vol_minus] = True

# dp[N]을 역순으로 탐색하면서 True가 몇 번째만에 나왔는지 구해서 M에서 뺌 -> 정답
try:
    print(M - operator.indexOf(reversed(dp[N]), True))
except ValueError:
    print(-1)
