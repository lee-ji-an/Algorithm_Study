import sys

N, K = map(int, sys.stdin.readline().split())
jaehan = [0] + list(map(int, sys.stdin.readline().split())) + [0]
dp = [0] * (N+1)  # dp[i] = i번째 먹이까지 조사했을 때 최대 에너지
# dp, jaehan 배열 모두 idx=1 부터 시작

left = right = 1
partsum = jaehan[left]

while (left <= N and right <= N):
    dp[right] = max(dp[right], dp[right-1])  # DP값 갱신

    # 구간합이 K 이상인 경우 left 전진
    if (partsum >= K):
        dp[right] = max(dp[right], dp[left-1] + partsum - K)  # 현재 최댓값 vs 새롭게 얻은 에너지
        if (left < right):
            partsum -= jaehan[left]
            left += 1
        elif (left == right):  # 구간합이 K보다 커서 left를 증가시키다가 같아졌을 경우 둘 다 전진
            left += 1
            right += 1
            partsum = jaehan[right]  # left == right and partsum >= K 이므로 새로 시작
    # 구간합이 K보다 작은 경우 right 전진
    else:
        right += 1
        partsum += jaehan[right]

print(dp[-1])

