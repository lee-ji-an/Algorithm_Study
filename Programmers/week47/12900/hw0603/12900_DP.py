def solution(n):
    C = 1_000_000_007
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % C
    
    answer = dp[n]
    return answer
