from collections import defaultdict
from itertools import accumulate
import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
mark = defaultdict(int)

cnt = 0
for accNum in accumulate(arr):  # 누적합을 순회
    if (accNum == K):  # 현재 누적합이 K인 경우 카운트 증가
        cnt += 1
    cnt += mark[accNum - K]  # (현재 누적합인 accNum) + (accNum-K) = K 인 경우의 수 만큼 카운트 증가

    mark[accNum] += 1  # 현재까지의 누적합의 경우 마킹

print(cnt)
