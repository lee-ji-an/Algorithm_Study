import sys
from collections import deque

input = sys.stdin.readline

dy = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)

M, N, H = map(int, input().split())
boxes = []
tomatoes_cnt = N * M * H   # tomatoes_cnt : 익혀야 하는 토마토 갯수
q = deque()


for i in range(H):
    box = []
    for j in range(N):
        row = list(map(int, input().split()))
        for k in range(M):
            if row[k] == 1:
                tomatoes_cnt -= 1
                q.append((j, k, i))  # 익은 토마토를 q에 저장
            elif row[k] == -1:
                tomatoes_cnt -= 1
        box.append(row)
    boxes.append(box)


def bfs(cnt):
    day = 0
    while q:
        day += 1
        for i in range(len(q)):
            y, x, z = q.popleft()
            for d in range(6):
                movey, movex, movez = y + dy[d], x + dx[d], z + dz[d]
                if not(0 <= movey < N) or not(0 <= movex < M) or not(0 <= movez < H):
                    continue
                # 주위 토마토 익히기
                if boxes[movez][movey][movex] == 0:
                    boxes[movez][movey][movex] = 1
                    cnt -= 1
                    q.append((movey, movex, movez))   # 새롭게 익은 토마토를 q에 저장
        if cnt == 0:
            return day

    return -1


if tomatoes_cnt == 0:
    print(0)
else:
    print(bfs(tomatoes_cnt))
