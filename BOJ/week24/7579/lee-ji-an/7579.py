import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

# bag[ i ][ cost ] => 0 ~ i번째 앱까지 봤을 때 cost의 비용으로 확보할 수 있는 최대 메모리 바이트
bag = [[-1] * (sum(C) + 1) for _ in range(N + 1)]
bag[0][0] = 0

# 0-1 knapsack 과 동일
for i in range(1, N + 1):
    for cost in range(sum(C) + 1):
        if bag[i - 1][cost] >= 0:
            if bag[i - 1][cost] > bag[i][cost]:
                bag[i][cost] = bag[i - 1][cost]
            if bag[i - 1][cost] < M and bag[i - 1][cost] + A[i] > bag[i][cost + C[i]]:
                bag[i][cost + C[i]] = bag[i - 1][cost] + A[i]

for cost in range(0, sum(C) + 1):
    if bag[N][cost] >= M:
        print(cost)
        break

