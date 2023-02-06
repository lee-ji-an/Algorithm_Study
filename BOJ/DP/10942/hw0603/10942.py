import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
dp = [[0]*N for _ in range(N)]  # dp[i][j] = nums[i:j+1]의 숫자가 팰린드롬인가?

# 길이가 1인 경우(=자기자신)는 무조건 팰린드롬
for i in range(N):
    dp[i][i] = 1

# 길이가 2인 경우는 두 숫자가 같을 때만 팰린드롬
for i in range(N-1):
    dp[i][i+1] = 1 if nums[i] == nums[i+1] else 0

# 길이가 3 이상일 경우 양 끝단의 숫자가 같으면서 start+1, end-1 의 dp값이 같을 때 팰린드롬
for cnt in range(N-2):
    for start in range(N-2-cnt):
        end = start+2+cnt
        if (nums[start] == nums[end] and dp[start+1][end-1] == 1):
            dp[start][end] = 1

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a-1][b-1])
