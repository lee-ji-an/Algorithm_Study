from bisect import bisect_left
import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
house = sorted(int(sys.stdin.readline().rstrip()) for _ in range(N))

start, end = 1, (house[-1] - house[0])  # 최소 간격과 최대 간격. end: 첫 집과 끝 집 사이의 거리

while (True):
    mid = (start + end) // 2

    init = house[0]
    initIdx = 0
    routerCnt = 0

    while (initIdx < N):
        routerCnt += 1
        initIdx = bisect_left(house, house[initIdx]+mid)

    if (routerCnt < C):
        end = mid - 1
    else:
        start = mid + 1
    
    # 더 큰 거리 간격을 구할 수 없을 때 정답 출력
    if (mid == end):
        print(mid)
        break
