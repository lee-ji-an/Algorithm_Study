import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())

no_road = set()
sub_cnt = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(K):
    a, b, c, d = map(int, input().split())
    no_road.add((a, b, c, d))


def check(x1, y1, x2, y2):
    if (x1, y1, x2, y2) in no_road or (x2, y2, x1, y1) in no_road:
        return False
    return True


for i in range(1, N + 1):
    if check(i-1, 0, i, 0):
        sub_cnt[i][0] = 1
    else:
        break
    sub_cnt[i][0] = 1 if check(i-1, 0, i, 0) else 0
for i in range(1, M + 1):
    if check(0, i-1, 0, i):
        sub_cnt[0][i] = 1
    else:
        break

for i in range(1, min(N, M) + 1):
    for x in range(i, N + 1):
        left = sub_cnt[x - 1][i] if check(x-1, i, x, i) else 0
        down = sub_cnt[x][i - 1] if check(x, i-1, x, i) else 0
        sub_cnt[x][i] = down + left
    for y in range(i + 1, M + 1):
        down = sub_cnt[i][y-1] if check(i, y-1, i, y) else 0
        left = sub_cnt[i-1][y] if check(i-1, y, i, y) else 0
        sub_cnt[i][y] = down + left

print(sub_cnt[N][M])
