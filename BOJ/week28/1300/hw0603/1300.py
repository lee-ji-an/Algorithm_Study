import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

start, end = 1, N*N
while (start <= end):
    mid = (start + end) // 2  # 중간값 찌름

    # 각 행에서 mid 이하 원소의 개수
    cnt = sum(
        min(mid//i, N) for i in range(1, N+1)
    )
    
    # mid 이하 원소의 개수가 K개 이상이면
    if (cnt >= K):
        ans = mid
        end = mid - 1  # 탐색범위 왼쪽으로
    else:
        start = mid + 1  # 탐색범위 오른쪽으로

print(ans)
