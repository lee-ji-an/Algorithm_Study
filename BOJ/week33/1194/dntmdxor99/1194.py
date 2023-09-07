import sys
from collections import deque
input = sys.stdin.readline


def bfs(dq):
    dist = -1
    while dq:
        dist += 1
        for _ in range(len(dq)):
            y, x, keys = dq.popleft()
            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and check[ny][nx][keys]:
                    match maps[ny][nx]:     # 구별함
                        case '#': continue

                        case '.': 
                            check[ny][nx][keys] = False
                            dq.append((ny, nx, keys))

                        case '1':
                            return dist + 1

                        case _:
                            if (k := maps[ny][nx]) in key:      # 키의 자리라면
                                newKeys = keys | key[k]     # or 연산을 통해 키를 획득함 -> 가지고 있어도 상관없음
                                if check[ny][nx][newKeys]:      # 방문한 전적이 있다면 패스
                                    check[ny][nx][newKeys] = False
                                    dq.append((ny, nx, newKeys))

                            elif (d := maps[ny][nx]) in door:       # 문이라면
                                if door[d] & keys:      # 그리고 키를 가지고 있다면
                                    check[ny][nx][keys] = False
                                    dq.append((ny, nx, keys))

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [list(input().rstrip()) for _ in range(n)]
    check = [[[True] * 2**6 for _ in range(m)] for _ in range(n)]
    dq = deque()
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    key = {'a' : 1, 'b' : 2, 'c' : 4, 'd' : 8, 'e' : 16, 'f' : 32}
    door = {'A' : 1, 'B' : 2, 'C' : 4, 'D' : 8, 'E' : 16, 'F' : 32}

    for y in range(n):
        for x in range(m):
            if maps[y][x] == '0':
                dq.append((y, x, 0))
                check[y][x][0] = False
                maps[y][x] = '.'
                break
        else:
            continue
        break

    print(bfs(dq))