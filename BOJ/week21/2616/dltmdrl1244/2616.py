import sys
input = sys.stdin.readline

n = int(input())
train = [0] + list(map(int, input().split()))
s = []
t = 0
k = int(input())
# dp[i][j] : 기관차를 i개 사용하면서 탐색한 마지막 객차가 j일 때의 최대 수용 인원수
dp = [[0 for _ in range(n+1)] for _ in range(4)]

# 구간합을 위한 누적합 구하기
for i in range(n+1):
    t += train[i]
    s.append(t)

# i : 이용하는 기관차 수
# j : 탐색한 객차 번호
for i in range(1, 4):
    for j in range(k*i, n+1):
        # j번째 객차를 선택하지 않거나 (dp[i][j-1]) 혹은 마지막 객차로 j를 선택 (즉 j-k번째부터 시작)
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + (s[j] - s[j-k]))

print(dp[3][n])