import sys

N, M = map(int, sys.stdin.readline().split())
Tk = [int(sys.stdin.readline()) for _ in range(N)]

result = max(Tk) * M  # 최대 시간으로 초기화

start, end = 0, result

while (start <= end):
    mid = (start + end) // 2

    # mid 라는 시간이 주어질 때, 각 심사대에서 최대로 처리 가능한 인원의 합을 구함
    total = sum(mid // t for t in Tk)

    # mid 시간만으로는 M명을 처리할 수 없는 경우(시간이 모자란 경우)
    if (total < M):
        start = mid + 1  # 탐색 범위를 mid의 우측으로 
    # mid 시간만 있어도 M명을 모두 처리할 수 있는 경우(시간이 딱 맞거나 넉넉한 경우)
    else:
        end = mid - 1  # 탐색 범위를 mid의 좌측으로
        result = min(result, mid)  # 최솟값 갱신

print(result)
