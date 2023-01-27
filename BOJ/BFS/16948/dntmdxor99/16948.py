from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dir = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

dq = deque([(r1, c1, 0)])
v = [1] * (n * n)
while dq:
    ri, ci, cnt = dq.popleft()
    for d in dir:
        rj, cj = ri + d[0], ci + d[1]       # 이동
        if 0 <= rj < n and 0 <= cj < n:     # 체스판을 벗어나면 안 됨
            if rj == r2 and cj == c2:       # 이동에 성공함
                print(cnt + 1)
                exit(0)
            if v[rj * n + cj]:      # 한 번도 방문하지 않았음
                dq.append((rj, cj, cnt + 1))        # 방문하지 않았으므로 추가함
                v[rj * n + cj] = 0      # 방문 표시
print(-1)