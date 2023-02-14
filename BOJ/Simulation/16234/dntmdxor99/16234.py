from collections import deque

n, l, r = map(int, input().split())
maps = [[m for m in map(int, input().split())] for _ in range(n)]
dq = deque()
new_dq = deque()
flag = True
cnt = -1
check = [[0] * n for _ in range(n)]
k = 0

while flag:
    flag = False
    for i in range(n):
        for j in range(n):
            if check[i][j] == k:
                dq.append([i, j])
                new_dq.clear()
                new_dq.append([i, j])
                sum = maps[i][j]
                check[i][j] = abs(k - 1)

                while dq:
                    y, x = dq.popleft()
                    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        if 0 <= (ny := y + dy) < n and 0 <= (nx := x + dx) < n:
                            if check[ny][nx] == abs(k - 1): continue
                            if l <= abs(maps[y][x] - maps[ny][nx]) <= r:
                                sum += maps[ny][nx]
                                dq.append([ny, nx])
                                new_dq.append([ny, nx])
                                check[ny][nx] = abs(k - 1)

                if (num := len(new_dq)) > 1:
                    avg = sum // num
                    for y, x in new_dq:
                        maps[y][x] = avg
                    flag = True

    cnt += 1
    k = abs(k - 1)
else:
    print(cnt)
