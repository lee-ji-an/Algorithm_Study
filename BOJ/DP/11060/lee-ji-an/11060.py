def solve():
    import sys
    input = sys.stdin.readline
    N = int(input())
    maze = list(map(int, input().split()))
    dp = [-1] * N
    dp[0] = 0
    for i in range(N):
        if dp[i] == -1:  # 현재 위치가 도달 가능한지 확인
            break
        for j in range(1, maze[i] + 1):
            if i + j >= N:
                break
            if dp[i + j] == -1:
                dp[i + j] = dp[i] + 1

    return dp[N - 1]


print(solve())
