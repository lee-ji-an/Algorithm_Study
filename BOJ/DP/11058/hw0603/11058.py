import sys

N = int(sys.stdin.readline())
dp = [i for i in range(N+1)]  # dp[i]: 버튼을 i번 눌러서 만들 수 있는 A의 최대 개수

for i in range(2, N+1):  # 버튼 2번 ~ N번에 대해 구함
    for j in range(2, i-1):  # 버튼을 i번 누를 때, j번째에 Ctrl-A, Ctrl-C, Ctrl-V.. (총 3+번)를 누르는 경우
        dp[i] = max(dp[i], dp[j] * (i-j-1))  # 최댓값 갱신 (전체선택 눌렀을 당시의 개수 * Ctrl-V 누를 수 있는 횟수)

print(dp[N])
