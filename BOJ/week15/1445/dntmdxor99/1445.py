import sys
from collections import deque
input = sys.stdin.readline


def sol(flag):
    # 다음 위치의 값과 현재 위치를 비교함
    i, j = ((0, 0), (1, 0), (0, 0), (0, 1))[flag]       # 현재 위치에 쓰레기, 인접한 곳에 쓰레기

    if ct[ny][nx] < ct[y][x] + i:
        return False  # 이전 + i이 가려는 곳보다 크면 갈 필요 없음

    elif ct[ny][nx] == ct[y][x] + i:  # 만약 같다면?
        if cat[ny][nx] <= cat[y][x] + j: return False  # 가려는 곳보다 이전이 같거나 크면 갈 필요 없음

    ct[ny][nx] = ct[y][x] + i
    cat[ny][nx] = cat[y][x] + j

    if flag:
        dq.append([ny, nx])

    return True


if __name__ == "__main__":
    n, m = map(int, input().split())
    maps = [list(input().strip()) for _ in range(n)]
    ct = [[2500] * m for _ in range(n)]        # check trash
    cat = [[2500] * m for _ in range(n)]       # check adjacent trash
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dq = deque()

    for y in range(n):
        for x in range(m):
            match maps[y][x]:
                case 'S':
                    dq.append([y, x])
                    ct[y][x] = cat[y][x] = 0

                case 'F':
                    out_y, out_x = y, x

                case '.':
                    for dy, dx in dir:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < m:
                            if maps[ny][nx] == 'g':     # 쓰레기 근처를 지날때 maps[y][x]를 a로 변경함
                                maps[y][x] = 'a'
                                break

    while dq:
        y, x = dq.popleft()

        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                match maps[ny][nx]:
                    case 'g':     # 쓰레기를 밟을 때
                        if not sol(1): continue

                    case '.':       # 땅을 밟을 때
                        if not sol(2): continue

                    case 'a':
                        if not sol(3): continue

                    case 'F':
                        if not sol(0): continue


    print(ct[out_y][out_x], cat[out_y][out_x])
