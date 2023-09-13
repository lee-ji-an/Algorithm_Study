import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dir = [[0, -1], [-1, 0], [0, 1]]

def bfs(y, x):
    if maps[y][x]:      # 바로 앞에 적이 있다면 먼저 쏨, 거리가 1인 적
        return True, y, x
    else:
        visited = set()
        visited.add((y, x))

        dq = deque()
        dq.append((y, x, 1))

        while dq:
            cy, cx, dist = dq.popleft()
            for dy, dx in dir:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < n and 0 <= nx < m:
                    if (dist < d):      # d보다 거리가 짧아야 쏠 수 있음
                        if (ny, nx) not in visited:
                            if maps[ny][nx]:
                                return True, ny, nx     # 쏠 수 있다면 반환
                            else:
                                dq.append((ny, nx, dist + 1))
                                visited.add((ny, nx))

        return False, -1, -1        # 쏠 수 있는 애가 없다면 False를 반환


def get_enemy(archers):
    enemy_set = set()
    cnt = 0

    for y in range(n - 1, -1, -1):      # 적이 내려오지말고, 궁수가 올라가면 됨
        enemy_set.clear()

        for x in archers:       # 궁수의 좌표
            flag, enemy_y, enemy_x = bfs(y, x)      # 적의 위치를 찾음

            if flag:
                enemy_set.add((enemy_y, enemy_x))       # 중복 처리, 같은 적을 쏠 수 있음

        cnt += len(enemy_set)

        for enemy_y, enemy_x in enemy_set:
            maps[enemy_y][enemy_x] = 0      # 적은 처리했음

    return cnt


if __name__ == "__main__":
    n, m, d = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    maps_original = [row[:] for row in maps]
    ans = 0

    for archers in combinations(range(m), 3):
        ans = max(ans, get_enemy(archers))
        maps = [row[:] for row in maps_original]        # 복구해야 됨

    print(ans)