from collections import deque
import sys

swan = deque()
water = deque()
H, W = map(int, sys.stdin.readline().split())
lake = [list(str(sys.stdin.readline().strip())) for _ in range(H)]
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)


for i in range(H):
    for j in range(W):
        if (lake[i][j] != "X"):
            water.append((i, j))  # 빙판이 아니라면 모두 물 공간
        if (lake[i][j] == "L"):
            swan.append((i, j))  # 백조 좌표 추가


def BFS(water, swan, W, H, lake):
    dest = swan.pop()  # 목적지 설정

    time = 1
    while (swan):
        # 1. 물 공간과 인접한 빙판을 모두 녹임
        temp = deque()
        while (water):
            row, col = water.popleft()
            for i in range(4):
                nr, nc = row+dr[i], col+dc[i]
                # 범위밖 Skip
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                # 빙판을 물로 만듦
                if (lake[nr][nc] == 'X'):
                    lake[nr][nc] = '.'
                    temp.append((nr, nc))
        water = temp

        temp = deque()
        while (swan):
            row, col = swan.popleft()

            # 다른 백조 좌표에 도달했다면 그때의 time 반환
            if ((row, col) == dest):
                return time

            for i in range(4):
                nr, nc = row+dr[i], col+dc[i]
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                
                # 백조가 갈 수 있는 공간이면서 아직 방문하지 않은 곳을 덱에 push
                if (lake[nr][nc] == '.' or lake[nr][nc] == 'L'):
                    lake[nr][nc] = time  # 방문처리. 꼭 값이 time이 아니여도 됨
                    swan.append((nr, nc))
                    temp.append((nr, nc))
        swan = temp
        time += 1
    
    return -1

print(BFS(water, swan, W, H, lake))
# print(*lake, sep='\n')