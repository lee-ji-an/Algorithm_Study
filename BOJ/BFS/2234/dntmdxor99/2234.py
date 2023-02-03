import sys
from collections import deque


def sol():
    m, n = map(int, sys.stdin.readline().split())
    board = [[b for b in map(int, sys.stdin.readline().split())] for _ in range(n)]
    check = [[0] * m for _ in range(n)]
    dir = [1, 2, 4, 8]      # 서, 북, 동, 남, 성곽 체크
    dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]       # 서, 북, 동, 남

    grp = 1
    cnt = dict()        # 구역의 개수
    adj = dict()        # 인접한 구격의 그룹 번호

    dq = deque()
    for i in range(n):
        for j in range(m):
            if check[i][j] == 0:
                dq.append([i, j])
                check[i][j] = grp       # 그룹 번호
                cnt[grp] = 1
                while dq:
                    y, x = dq.popleft()
                    for idx in range(4):
                        ny, nx = y + dy[idx], x + dx[idx]
                        if 0 <= ny < n and 0 <= nx < m:
                            if not board[y][x] & dir[idx]:      # 벽이 아니라면
                                if check[ny][nx] == 0:
                                    check[ny][nx] = grp     # 그룹 번호 입력
                                    cnt[grp] += 1       # 그룹의 개수 추가
                                    dq.append([ny, nx])
                            else:       # 벽인 경우
                                if check[ny][nx] != 0 and grp != check[ny][nx]:     # 방문했었고, 그룹 번호를 추가하지 않았다면
                                    adj[grp] = adj.get(grp, set()) | set([check[ny][nx]])
                grp += 1

    maximum = -1
    for i in adj.keys():
        for j in adj[i]:
            temp = cnt[i] + cnt[j]      # 인접한 애들을 싹 돌면서 최댓값을 갱신함
            maximum = temp if temp > maximum else maximum

    print(max(cnt.keys()))
    print(max(cnt.values()))
    print(maximum)

    return

sol()