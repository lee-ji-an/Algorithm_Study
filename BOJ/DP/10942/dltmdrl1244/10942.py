import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[None] * (n+1) for _ in range(n+1)]


for i in range(1, n):
    # 1개짜리는 무조건 팰린드롬
    dp[i][i] = 1
    # 2개짜리는 바로 옆칸이 같으면 팰린드롬
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

dp[n][n] = 1

for i in range(1, n):
    for j in range(1, n//2 + 1):
        # 홀수 개수 (3, 5, 7...)의 팰린드롬 여부
        if i+j > n or i-j < 0:
            continue
        # 기준점 i에서 j만큼 떨어진 원소가 같고, 앞 뒤 한칸씩 늘리기 전의 배열이 팰린드롬이었으면 팰린드롬
        if arr[i+j] == arr[i-j] and dp[i-j+1][i+j-1] == 1:
            dp[i-j][i+j] = 1
        else:
            dp[i-j][i+j] = 0

        # 짝수 개수 (2, 4, 6...)의 팰린드롬 여부
        if i+j+1 > n:
            continue
        # 기준점 i와 i+1에서 j만큼 떨어진 원소가 같고, 앞 뒤 한칸씩 늘리기 전의 배열이 팰린드롬이었으면 팰린드롬
        if arr[i+1+j] == arr[i-j] and dp[i-j+1][i+j] == 1:
            dp[i-j][i+1+j] = 1
        else:
            dp[i-j][i+1+j] = 0

m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])