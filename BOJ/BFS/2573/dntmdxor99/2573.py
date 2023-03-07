import sys
from collections import deque


def melt():
    # 빙산의 녹음을 구현한 함수
    adj_list = list(adj.items())
    for (y, x), cnt in adj_list:
        maps[y][x] = max(maps[y][x] - cnt, 0)
        if maps[y][x] == 0:
            adj.pop((y, x))     # 만약 모두 녹았다면 이제 인접한 바다가 있는지 체크할 필요가 없음

    for (y, x) in adj.keys():
        adj[(y, x)] = 0
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 0:
                    adj[(y, x)] += 1        # 다시 인접한 바다의 개수를 셈


def group():
    if len(adj) == 0:       # 만약 모두 녹기 전까지 분리된 적이 없다면 -1를 반환함
        return -1

    dq.append(list(adj.keys())[0])      # 맨 처음 좌표를 넣음
    check = set()

    while dq:
        y, x = dq.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in check:
                if maps[ny][nx]:
                    dq.append((ny, nx))
                    check.add((ny, nx))

    if len(check) != len(adj):      # 두 개의 개수가 다르면 2덩이 이상으로 나뉘어진 것이므로 그대로 반환함
        return True

    return False


def sol():
    cnt = 1
    while True:
        melt()
        match group():
            case True:
                return cnt
            case False:
                cnt += 1
            case -1:
                return 0


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    maps = [[m for m in map(int, input().split())] for _ in range(n)]
    adj = dict()
    dq = deque()

    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for y in range(n):
        for x in range(m):
            if maps[y][x]:
                adj[(y, x)] = 0
                for dy, dx in dir:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < m:
                        if maps[ny][nx] == 0:
                            adj[(y, x)] += 1        # 인접한 바다의 개수를 셈

    print(sol())