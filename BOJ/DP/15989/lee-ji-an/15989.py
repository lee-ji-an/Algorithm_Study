def solve():
    import sys
    input = sys.stdin.readline
    T = int(input())
    question = []
    dp = [0] * 10001
    for i in range(T):
        question.append(int(input()))
    max_q_num = max(question)

    dp[1], dp[2], dp[3] = (1, 0, 0), (1, 1, 0), (2, 0, 1)
    for i in range(4, max_q_num + 1):
        dp[i] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2], dp[i - 2][1] + dp[i - 2][2], dp[i - 3][2])

    for q in question:
        print(dp[q][0] + dp[q][1] + dp[q][2])


solve()
