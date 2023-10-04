import sys
input = sys.stdin.readline


if __name__ == "__main__":
    maps = input().strip()
    n = len(maps)
    isPalin = [[0] * n for _ in range(n)]
    dp = [sys.maxsize] * (n + 1)
    dp[-1] = 0

    for i in range(n):      # 길이가 1인 애는 팰린드롬임
        isPalin[i][i] = 1

    for i in range(n - 1):      # 길이가 2라면 앞뒤가 같아야 팰린드롬임
        if maps[i] == maps[i + 1]:
            isPalin[i][i + 1] = 1

    for l in range(3, n + 1):       # 아래는 dp를 통해 체크할 수 있음
        for start in range(n - l + 1):
            end = start + l - 1
            if maps[start] == maps[end] and isPalin[start + 1][end - 1]:
                isPalin[start][end] = 1

    for end in range(n):        # 생성된 팰린드롬 Dp를 사용해서 최소 개수의 dp를 사용했음
        for start in range(n):
            if isPalin[start][end]:
                dp[end] = min(dp[end], dp[start - 1] + 1)      
            else:
                dp[end] = min(dp[end], dp[end - 1] + 1)

    print(dp[n - 1])