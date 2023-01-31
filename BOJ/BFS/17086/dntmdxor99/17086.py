import sys
import itertools

def sol():
    n, m = map(int, sys.stdin.readline().split())
    max_index = max(n, m)
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    maximum = 1
    for y in range(n):
        for x in range(m):
            dist = maximum      # dist는 아기상어와의 최대 거리임, 초기값은 1
            if not board[y][x]:
                while dist < max_index:     # 안전거리는 max(n, m) 보다 클 수 없음
                    if 1 in itertools.chain(*[board[ny][0 if x - dist < 0 else x - dist: x + dist + 1] for ny in range(0 if y - dist < 0 else y - dist, min(n, y + dist + 1))]):
                        # 특정 좌표 기준 정사각형을 모두 긁어와서, 만약 1(아기 상어)이 있다면 최대 거리를 수정하고, 다른 좌표로 넘어감
                        maximum = dist if maximum < dist else maximum       # 아기 상어가 있다면 최대 거리를 수정함
                        break
                    dist += 1       # 안전 거리에 아기 상어가 없다면 안전 거리를 늘림
                else:
                    maximum = dist - 1 if maximum < dist - 1 else maximum       # while문이 False가 되어 끝난다면 최대 거리를 수정함 
    print(maximum)

sol()
