from collections import deque
import sys


def sol(dq : deque):
    global empty
    cnt = 1
    while dq:
        for _ in range(len(dq)):
            z, y, x = dq.popleft()
            for dz, dy, dx in dir:
                nz, ny, nx = z + dz, y + dy, x + dx
                if not (0 <= nz < h and 0 <= ny < n and 0 <= nx < m):
                    continue
                if maps[nz][ny][nx] == 0:       # 익지 않은 토마토라면
                    maps[nz][ny][nx] = 1        # 익힘
                    dq.append((nz, ny, nx))     # 덱에 넣음
                    empty -= 1      # 숫자를 하나씩 줄임

        if empty == 0:      # 0이라면 리턴함
            return cnt

        cnt += 1

    return -1


if __name__ == "__main__":
    input = sys.stdin.readline
    m, n, h = map(int, input().split())
    maps = [[[m for m in map(int, input().split())] for _ in range(n)] for _ in range(h)]
    dq = deque()

    dir = [[0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]
    empty = 0

    for i in range(h):
        for j in range(n):
            for k in range(m):
                match maps[i][j][k]:
                    case 0:
                        empty += 1      # 익지 않은 토마토의 개수를 셈
                    case 1:
                        dq.append((i, j, k))        # 덱에 넣음

    if empty == 0:
        print(0)
        exit(0)

    print(sol(dq))
