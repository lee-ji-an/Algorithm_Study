from collections import deque
import copy
import sys

N, M = map(int, sys.stdin.readline().split())
board = []
coin = deque()
visited = set()
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
COIN, EMPTY, WALL = 0, 1, 2

# 보드 입력받으면서 두 동전의 좌표 저장
for i in range(N):
    board.append(list(sys.stdin.readline().strip()))
    for j in range(M):
        if (board[i][j] == 'o'):
            coin.append((i, j))
            board[i][j] = EMPTY
        elif (board[i][j] == '.'):
            board[i][j] = EMPTY
        elif (board[i][j] == '#'):
            board[i][j] = WALL

visited.add(''.join(map(str, coin)))  # visited 정보는 문자열로 관리


def bfs():
    cnt = 0
    q = deque([coin])

    while (q):
        for _ in range(len(q)):
            now = q.popleft()
            # 버튼을 10번 눌러도 동전이 떨어지지 않는 경우 -1 출력
            if (cnt == 10):
                return -1
            
            for i in range(4):
                # 4가지 방향에서 독립적인 시뮬레이션을 위해 깊은 복사
                temp = copy.deepcopy(now)

                # 두 동전을 움직임
                for _ in range(2):
                    r, c = temp.popleft()
                    nr, nc = r+dr[i], c+dc[i]

                    if not (0 <= nr < N and 0 <= nc < M):  # 보드 범위 밖 Skip
                        continue

                    match (board[nr][nc]):
                        case 1:  # 새 좌표가 빈 칸이면 이동
                            temp.append((nr, nc))
                        case 2:  # 새 좌표가 벽이면 이동하지 못함 -> 기존 좌표 append
                            temp.append((r, c))

                # 시뮬레이션 후 동전 개수 체크
                match (len(temp)):
                    case 0:  # 동전 개수가 0개이면(동전 두 개가 모두 떨어진 경우) continue
                        continue
                    case 1:  # 동전 개수가 1개이면(동전 하나가 떨어졌다면) 종료
                        return cnt + 1
                    case 2:  # 두 동전이 모두 보드 위에 있는 경우 방문처리 후 BFS 큐에 추가
                        visit_str = ''.join(map(str, temp))
                        if (visit_str not in visited):
                            visited.add(visit_str)
                            q.append(temp)
                
        cnt += 1
    
    return -1  # 동전을 떨어뜨릴 수 없는 경우

print(bfs())
