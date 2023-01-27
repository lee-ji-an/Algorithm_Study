import sys
from collections import deque
input = sys.stdin.readline

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

n = int(input())
board = []
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 9:
            curpos = [i, j]
            tmp[j] = 0
    board.append(tmp)

cur_size = 2
cur_exp = 0
ans = 0

def bfs(pos):
    q = deque()
    q.append((pos[0], pos[1], 0))
    visited = [[False] * n for _ in range(n)]
    visited[pos[0]][pos[1]] = True
    fishes = []
    mindist = float('inf')

    while q:
        cy, cx, cnt = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx] <= cur_size and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, cnt + 1))
                    # 후보들을 정하기 위해 일단 fishes 리스트에 넣어둔다. 이 때 기준점을 잡아 거리가 mindist 이하인 것만 넣어준다.
                    if 0 < board[ny][nx] < cur_size and cnt + 1 <= mindist:
                        mindist = cnt + 1
                        fishes.append([ny, nx, cnt + 1])

    '''
    fishes 리스트 중에서
    1. 거리가 가장 짧은 먹이
    2. y좌표가 가장 작은 먹이
    3. x좌표가 가장 작은 먹이
    와 같은 순서대로 기준을 정렬하였을 때 처음에 오는 위치에 있는 먹이가 다음에 먹어야 할 먹이이다.
    '''
    if fishes:
        fishes.sort(key = lambda x: (x[2], x[0], x[1]))
        return fishes[0][0], fishes[0][1], fishes[0][2]

    # 만약 fishes 배열이 비어있다면 (즉 먹이를 하나도 찾지 못했다면)
    return -1, -1, -1

while True:
    # 먹이를 찾지 못하면 ny, nx에 -1, -1이 반환되어 종료된다.
    ny, nx, cnt = bfs(curpos)
    if (ny, nx) == (-1, -1):
        break

    # 먹이를 찾았다면 물고기를 없애고, 카운트를 올려주고 현재 위치를 옮겨준다.
    board[ny][nx] = 0
    cur_exp += 1
    ans += cnt
    curpos = [ny, nx]

    # 레벨업
    if cur_exp == cur_size:
        cur_size += 1
        cur_exp = 0

print(ans)