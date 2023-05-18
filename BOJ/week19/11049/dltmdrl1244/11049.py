import sys
input = sys.stdin.readline

n = int(input())
matrixes = [list(map(int, input().split())) for _ in range(n)]
# dp[i][j] : 행렬 i ~ j까지를 최소 비용으로 곱할 때 연산 횟수
dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]

# 자기자신을 만드는 비용은 0
for i in range(n):
    dp[i][i] = 0

'''
n = 6
01 12 23 34 45
02 13 24 35
02 -> dp[0][0] + dp[1][2] / dp[0][1] + dp[2][2]
행렬 0~0 만드는 비용 + 행렬 1~2만드는 비용 + 둘 합치는 비용
행렬 0~1 만드는 비용 + 행렬 2+2만드는 비용 + 둘 합치는 비용
03 14 25
03 -> dp[0][0] + dp[1][3] / dp[0][1] + dp[2][3] / dp[0][2] + dp[3][3]
04 25
05
'''

for j in range(1, n):
    for i in range(n-j):
        # 중간 지점 k 
        for k in range(i, i+j):
            dp[i][i+j] = min(dp[i][i+j], dp[i][k] + dp[k+1][i+j] + matrixes[i][0] * matrixes[k+1][0] * matrixes[i+j][1])

print(dp[0][n-1])