import sys
input = sys.stdin.readline

N = int(input())
order = int(input())

ans = 0
start, end = 1, N * N
while start <= end:
    mid = (start + end) // 2

    # max_cnt = mid 보다 작거나 같은 숫자의 갯수
    max_cnt = sum(min(mid // i, N) for i in range(1, N + 1))

    # 정답 찾으면 종료
    if order <= max_cnt:
        ans = mid

    if order > max_cnt:
        start = mid + 1
    else:
        end = mid - 1

print(ans)
