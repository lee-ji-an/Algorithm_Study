from collections import deque


def bfs():
    while dq:
        y1, x1, y2, x2, cnt = dq.popleft()
        if cnt >= 10:
            return -1
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny1, nx1 = y1 + dy, x1 + dx
            ny2, nx2 = y2 + dy, x2 + dx
            if 0 <= ny1 < n and 0 <= nx1 < m and 0 <= ny2 < n and 0 <= nx2 < m:
                if maps[ny1][nx1] == '#':
                    ny1, nx1 = y1, x1
                if maps[ny2][nx2] == '#':
                    ny2, nx2 = y2, x2
                dq.append([ny1, nx1, ny2, nx2, cnt + 1])
            elif not (0 <= ny1 < n and 0 <= nx1 < m) and not(0 <= ny2 < n and 0 <= nx2 < m):
                continue
            else:
                return cnt + 1
    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [list(input()) for _ in range(n)]
    tp = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'o':
                tp.append(i)
                tp.append(j)
    dq = deque()
    dq.append([*tp, 0])

    print(bfs())