import sys

N = int(sys.stdin.readline())
matrix = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]  # dp[i][j] = i ~~~ j chain의 행렬 곱셈 연산 횟수 최솟값


for matrixNum in range(N-1):  # matrixNum: 대각선 한 줄
    for i in range(N-1-matrixNum):  # i: 대각선 안의 원소들
        j = i+matrixNum+1
        dp[i][j] = sys.maxsize  # MAX값 초기화해 두고
        for k in range(i, j):  # 모든 chain의 경우 중 최솟값 구하기
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0]*matrix[k][1]*matrix[j][1])

print(dp[0][-1])
