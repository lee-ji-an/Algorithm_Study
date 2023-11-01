def solution(x, y, n):
    dp = [-1] * (y + 1)
    dp[x] = 0

    # dp 배열을 x ~ y까지 차례대로 탐색 -> dp 배열을 채움
    #  +n / *2 / *3 모두 현재 x 값보다 값을 더 증가시키는 연산이기 때문
    for i in range(x, y + 1):
        # dp[i] 가 -1이면 도달할 수 없는 수이므로 통과
        if dp[i] == -1:
            continue

        # x + n
        if i + n <= y and (dp[i + n] == -1 or dp[i + n] > dp[i] + 1):
            dp[i + n] = dp[i] + 1
        # x * 2
        if i * 2 <= y and (dp[2 * i] == -1 or dp[2 * i] > dp[i] + 1):
            dp[i * 2] = dp[i] + 1
        # x * 3
        if i * 3 <= y and (dp[3 * i] == -1 or dp[3 * i] > dp[i] + 1):
            dp[i * 3] = dp[i] + 1

    return dp[y]
