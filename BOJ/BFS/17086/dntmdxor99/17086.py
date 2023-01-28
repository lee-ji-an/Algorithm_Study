import sys
import itertools

def sol():
    n, m = map(int, sys.stdin.readline().split())
    max_index = max(n, m)
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    maximum = 1
    for y in range(n):
        for x in range(m):
            dist = maximum
            if not board[y][x]:
                while dist < max_index:
                    if 1 in itertools.chain(*[board[ny][0 if x - dist < 0 else x - dist: x + dist + 1] for ny in range(0 if y - dist < 0 else y - dist, min(n, y + dist + 1))]):
                        maximum = dist if maximum < dist else maximum
                        break
                    dist += 1
                else:
                    maximum = dist - 1 if maximum < dist - 1 else maximum
    print(maximum)

sol()
