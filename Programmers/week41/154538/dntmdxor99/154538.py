def solution(x, y, n):
    dp = [float('inf')] * (y + 1)
    dp[x] = 0
    
    for i in range(x, max(y - n, y // 3) + 1):      # 범위에 제한을 줌
        # 인덱스를 벗어나지 않으면 최솟값을 구함
        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
            if i * 3 <= y:
                dp[i * 3] = min(dp[i * 3], dp[i] + 1)
        # 인덱스를 벗어나면 continue함
    
    return -1 if dp[y] == float('inf') else dp[y]