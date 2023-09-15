import sys
from collections import deque
input = sys.stdin.readline


def find_start_end_coordinate():
    for y in range(n):
        for x in range(n):
            if maps[y][x] == 'B':
                if x < n - 1 and maps[y][x + 1] == 'B':
                    sy = y
                    sx = x + 1
                    maps[y][x] = maps[y][x + 1] = maps[y][x + 2] = '0'
                    sf = 1
                elif y < n - 1 and maps[y + 1][x] == 'B':
                    sy = y + 1
                    sx = x
                    maps[y][x] = maps[y + 1][x] = maps[y + 2][x] = '0'
                    sf = 2
            elif maps[y][x] == 'E':
                if x < n - 1 and maps[y][x + 1] == 'E':
                    ey = y
                    ex = x + 1
                    maps[y][x] = maps[y][x + 1] = maps[y][x + 2] = '0'
                    ef = 1
                elif y < n - 1 and maps[y + 1][x] == 'E':
                    ey = y + 1
                    ex = x
                    maps[y][x] = maps[y + 1][x] = maps[y + 2][x] = '0'
                    ef = 2

    return sy, sx, sf, ey, ex ,ef


def can_it_go(y, x, flag, rotation = False):
    if rotation:
        flag = (0, 2, 1)[flag]      # 회전하므로 flag를 변환함
        if visited[y][x] & flag: return False       # 비트 연산으로 방문 체크
        if x == 0 or x == n - 1 or y == 0 or y == n - 1: return False       # 범위를 넘어가면 안 됨
        if sum([int(i) for r in range(y - 1, y + 2) for i in maps[r][x - 1 : x + 2]]): return False     # 가로세로 둘 다 비어있어야 함. flag까지 고려하려면 코드가 길어져서 그냥 전체 다 확인함
    else:
        if visited[y][x] & flag: return False
        else:
            if flag == 1:
                if x == 0 or x == n - 1: return False
                if maps[y][x - 1] or maps[y][x + 1]: return False
            elif flag == 2:
                if y == 0 or y == n - 1: return False
                if maps[y - 1][x] or maps[y + 1][x]: return False
    
    return True


def bfs(dq):
    cnt = 0
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]
    while dq:
        cnt += 1
        for _ in range(len(dq)):
            y, x, flag = dq.popleft()
            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] == 0:
                    rotation = not (dy | dx)        # 변환을 해야하는지 체크
                    if can_it_go(ny, nx, flag, rotation = rotation):
                        flag = (3 ^ flag) if rotation else flag     # 변환하면 변환한 것으로 flag 교체
                        if (ny, nx, flag) == (ey, ex, ef):      # 목적지에 도착하면 반환
                            return cnt
                        else:
                            visited[ny][nx] |= flag     # 비트 or 연산으로 방문 표시
                            dq.append((ny, nx, flag))

    return 0
        

if __name__ == "__main__":
    n = int(input())
    maps = [list(input().strip()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]       # 0, 1, 2, 3 각각 미방문, 가로, 세로, 가로세로

    sy, sx, sf, ey, ex, ef = find_start_end_coordinate()
    maps = [list(map(int, row[:])) for row in maps]
    
    dq = deque()
    dq.append((sy, sx, sf))

    print(bfs(dq))