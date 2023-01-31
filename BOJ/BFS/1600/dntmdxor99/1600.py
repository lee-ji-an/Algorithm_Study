import sys
from collections import deque


def sol():
    k = int(sys.stdin.readline())
    w, h = map(int, sys.stdin.readline().split())
    board = [[b for b in map(int, sys.stdin.readline().split())] for _ in range(h)]
    check = [[k + 1 for _ in range(w)] for _ in range(h)]

    dq = deque([[0, 0, 0]])
    dy, dx = [-1, 0, 0, 1], [0, 1, -1, 0]
    h_dy, h_dx = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]     # 말을 타는 경우
    cnt = 1

    while dq:
        for _ in range(len(dq)):
            y, x, cur_k = dq.popleft()
            if y == h - 1 and x == w - 1:
                print(cnt - 1)
                exit(0)
            if cur_k < k:       # 아직 임계치까지 말을 타지 않은 경우
                for i in range(8):
                    ny, nx = y + h_dy[i], x + h_dx[i]
                    if 0 <= ny < h and 0 <= nx < w and check[ny][nx] > cur_k + 1 and not board[ny][nx]:
                        # 기존에 방문한 곳보다 말을 적게 탔을 경우도 확인해야 함
                        dq.append([ny, nx, cur_k + 1])
                        check[ny][nx] = cur_k + 1
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < h and 0 <= nx < w and check[ny][nx] > cur_k and not board[ny][nx]:
                    # 기존에 방문한 곳보다 말을 적게 탔을 경우도 확인해야 함
                    dq.append([ny, nx, cur_k])
                    check[ny][nx] = cur_k

        cnt += 1
    print(-1)


sol()
