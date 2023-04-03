import sys

N = int(sys.stdin.readline())
data = sorted(
    (tuple(map(int, sys.stdin.readline().split())) for _ in range(N)),
    key=lambda x: x[1],
    reverse=True  # 마감 기한이 늦은 일 부터 조사
)

cur = sys.maxsize
for delay, due in data:
    cur = min(cur, due) - delay

print(-1 if cur < 0 else cur)
