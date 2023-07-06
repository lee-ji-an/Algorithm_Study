import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())

    maps = [[0] * n for _ in range(n)]      # 갈 수 없음

    pair = dict()

    for _ in range(m):
        x, y, a, b = map(int, input().split())
        x, y, a, b = x - 1, y - 1, a - 1, b - 1

        maps[b][a] = 2      # 지금은 불이 꺼져있지만, 언젠가는 갈 수 있을지도 모르는 애들

        pair[(b, a)] = pair.get((b, a), [])     # b, a의 불을 킬 수 있는 애들 -> y, x
        pair[(b, a)].append((y, x))

    maps[0][0] = 1  # 갈 수 있음
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    dq = deque([[0, 0]])
    after = set()       # 지금은 불이 꺼져있지만, 언젠가는 갈 수 있을지도 모르는 애들

    flag = True
    while flag:     # 만약 False라면 갈 수 있는 곳이 한 군데도 없음, True라면 혹시 모름
        while dq:       # 지금 당장 갈 수 있는 애들은 모두 갈 거임
            flag = False
            for _ in range(len(dq)):
                y, x = dq.popleft()
                if maps[y][x] == 1:      # 해당 방에 갈 수 있음
                    for dy, dx in dir:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < n:
                            if maps[ny][nx] == 2:        # 일단 불은 꺼져 있는데, 아래의 명령어에 의해 갈 수 있을지 없을지 결정됨
                                for b, a in pair[(ny, nx)]:     # ny, nx의 불을 킬 수 있는 후보군들
                                    if maps[b][a] == 1:     # ny, nx의 불을 킬 수 있음
                                        flag = True     # 갈 수 있는 곳이 존재했었음
                                        maps[ny][nx] = 1        # 불을 키고 방문
                                        dq.append((ny, nx))     # 갈 수 있음
                                    elif maps[b][a] == 2:       # ny, nx의 방을 나중에라도 킬 수 있을지도 모름
                                        after.add((y, x))       # 일단은 저장

        if len(after):      # 만약 나중에라도 킬 수 있다면
            flag = True
            dq = deque(after)
            after.clear()

    ans = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                ans += 1

    print(ans)
