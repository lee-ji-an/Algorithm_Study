from collections import deque
from bisect import bisect_left
import sys

dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

# 로봇 청소기의 좌표를 전달받고 더러운 칸을 모두 청소하기 위한 이동 횟수 최솟값 반환
def bfs(initRow, initCol, trash) -> tuple:
    ALL_ON = (1 << len(trash)) - 1  # 더러운 방 개수만큼의 모든 비트가 켜진 정수
    visited = [[set() for _ in range(W)] for _ in range(H)]  # (row, col)에 도착했을 때, 각 경로에서 청소한 더러운 칸의 index 정보가 담긴 비트열이 저장되는 집합
    q = deque([(initRow, initCol, 0)])  # row, col, clean_bit
    dist = 0
    
    while (q):
        for _ in range(len(q)):
            row, col, clean_bit = q.popleft()  # clean_bit: 현재 경로에서 지금까지 청소한 더러운 칸의 index 정보
            
            # 4방향 탐색
            for i in range(4):
                nrow, ncol = row+dr[i], col+dc[i]

                # room 범위 밖이면 Skip
                if not (0 <= nrow < H and 0 <= ncol < W):
                    continue
                # 가구가 있는 칸이면 Skip
                if (room[nrow][ncol] == WALL):
                    continue
                
                # 더러운 칸이면
                if (room[nrow][ncol] == DIRTY):
                    # 현재 더러운 칸이 trash 배열의 몇 번째 인덱스에 있는지 찾아서 bit shift 후 OR 연산
                    next_bit = clean_bit | (1 << bisect_left(trash, (nrow, ncol)))
                    '''모든 비트가 켜져 있다면 청소 완료'''
                    if (next_bit == ALL_ON):
                        return dist+1
                    # 다음 좌표에 아직 방문하지 않았을 때
                    if not (next_bit in visited[nrow][ncol]):
                        q.append((nrow, ncol, next_bit))  # 다음 좌표 삽입. 청소하고 갈 것이므로 next_bit로 삽입
                        visited[nrow][ncol].add(next_bit)
                # 빈 칸이고
                else:
                    # 방문하지 않았을 때
                    if not (clean_bit in visited[nrow][ncol]):
                        q.append((nrow, ncol, clean_bit))  # 다음 좌표 삽입. 청소하지 않았으므로 clean_bit는 그대로 삽입
                        visited[nrow][ncol].add(clean_bit)
        
        dist += 1

    return -1  # 방문할 수 없는 더러운 칸이 존재하는 경우


EMPTY, WALL, DIRTY = 0, 1, 9
while (True):
    W, H = map(int, sys.stdin.readline().split())
    if ((W, H) == (0, 0)):
        break
    room = [[0]*W for _ in range(H)]
    robotPos = (-1, -1)
    trash = []
    
    for i in range(H):
        line = list(sys.stdin.readline().rstrip())
        for j in range(W):
            match (line[j]):
                case 'o':
                    robotPos = (i, j)
                    room[i][j] = EMPTY
                case '.':
                    room[i][j] = EMPTY
                case 'x':
                    room[i][j] = WALL
                case '*':
                    trash.append((i, j))
                    room[i][j] = DIRTY
    
    print(bfs(*robotPos, sorted(trash)))
