import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [list(input().strip()) for _ in range(n)]
    ct = [[2500] * m for _ in range(n)]        # check trash
    cat = [[2500] * m for _ in range(n)]       # check adjacent trash
    adj = [[0] * m for _ in range(n)]
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dq = deque()

    for y in range(n):
        for x in range(m):
            if maps[y][x] == 'S':
                dq.append([y, x])
                ct[y][x] = cat[y][x] = 0
            elif maps[y][x] == 'F':
                out_y, out_x = y, x
            elif maps[y][x] == '.':
                for dy, dx in dir:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < m:
                        if maps[ny][nx] == 'g':     # 쓰레기 근처를 지날때 adj를 1로 변경함
                            adj[y][x] = 1
                            break

    while dq:
        y, x = dq.popleft()

        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 'g':     # 쓰레기를 밟을 때
                    if ct[ny][nx] < ct[y][x] + 1: continue      # 이전 + 1이 가려는 곳보다 크면 갈 필요 없음
                    elif ct[ny][nx] == ct[y][x]:        # 만약 같다면?
                        if cat[ny][nx] <= cat[y][x]: continue       # 가려는 곳보다 이전이 같거나 크면 갈 필요 없음

                    ct[ny][nx] = ct[y][x] + 1
                    cat[ny][nx] = cat[y][x]
                    dq.append([ny, nx])

                elif maps[ny][nx] == '.':       # 땅을 밟을 때
                    if ct[ny][nx] < ct[y][x]: continue      # 이전이 가려는 곳보다 쓰레기 값이 크다면 갈 필요 없음
                    if ct[ny][nx] == ct[y][x]:
                        if cat[ny][nx] <= cat[y][x] + adj[ny][nx]: continue     # 가려는 곳보다 이전의 인접한 쓰레기 개수가 크거나 같다면 갈 필요 없음

                    ct[ny][nx] = ct[y][x]
                    cat[ny][nx] = cat[y][x] + adj[ny][nx]
                    dq.append([ny, nx])

                elif maps[ny][nx] == 'F':
                    if ct[ny][nx] < ct[y][x]: continue
                    elif ct[ny][nx] == ct[y][x]:
                        cat[ny][nx] = min(cat[ny][nx], cat[y][x])
                    elif ct[ny][nx] > ct[y][x]:
                        ct[ny][nx] = ct[y][x]
                        cat[ny][nx] = cat[y][x]

    print(ct[out_y][out_x], cat[out_y][out_x])
