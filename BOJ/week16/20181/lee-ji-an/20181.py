import sys
input = sys.stdin.readline

N, K = map(int, input().split())
food = list(map(int, input().split()))
food.append(0)
energy = []
dp = [0] * (N+1)
ans = 0

start = 0
end = 0
total = 0
while end < N:
    if total < K:
        while total < K and end < N:  # K 보다 커질 때까지 end를 뒤로 미루기
            total += food[end]
            end += 1
            dp[end] = max(dp[end], dp[end-1])
    while total >= K:  # K 보다 작아질 때까지 start를 뒤로 미루기
        dp[end] = max(dp[end], dp[start] + (total - K))
        total -= food[start]
        start += 1

print(dp[N])
