from collections import deque
from dataclasses import dataclass
import operator
import sys

N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 체스보드 색 정보
piece_pos = [[deque() for _ in range(N)] for _ in range(N)]  # 실제 말이 쌓여있는 체스보드
direction_delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 좌, 우, 상, 하

@dataclass
class Piece:
    idx: int = 0  # 말 번호
    pos: tuple[int, int] = (0, 0)
    dir: int = 0  # 0~3: 우, 좌, 상, 하

# 말 정보 저장
piece_list = [None]
for i in range(1, K+1):
    row, col, dir = map(lambda x: int(x)-1, sys.stdin.readline().split())
    piece_pos[row][col].append(i)
    piece_list.append(Piece(idx=i, pos=(row, col), dir=dir))


def move(src: tuple, dst: tuple, case: int=0):
    """
    다음 칸으로 이동. 해당 칸에 말이 존재하는 경우 가장 위에 올림
    case 0: dst가 흰 칸인 경우 -> 그냥 이동 -> queue
    case 1: dst가 빨간 칸인 경우 -> 이동 후 이동한 말들의 순서 반대로 바꿈 -> stack
    """
    r, c, nr, nc = *src, *dst

    # 내 위의 말들과 같이 한 번에 다음 칸으로 이동
    buffer = deque()
    addbuffer = buffer.append if not case else buffer.appendleft  # case에 따라 queue/stack 중 사용할 것 설정
    for idx in range(len(piece_pos[r][c])):
        targetIdx = piece_pos[r][c][idx]
        piece_list[targetIdx].pos = dst  # 위치 변경
        addbuffer(piece_list[targetIdx].idx)
    piece_pos[nr][nc] += buffer  # deque concatination
    # 가장 아랫쪽의 말과 함께 전부 이동하므로 이동 후에는 칸이 비워짐
    piece_pos[r][c].clear()


def simulation():
    for cnt in range(1000):
        # 1번 말 ~ K번 말을 순서대로 이동
        for p in piece_list[1:]:
            r, c = p.pos  # 현재 말의 좌표
            nr, nc = map(operator.add, p.pos, direction_delta[p.dir])  # 다음 이동할 칸
            nextPosColor = board[nr][nc] if 0 <= nr < N and 0 <= nc < N else 2  # 다음 이동할 칸의 색. 범위 밖은 BLUE와 같은 경우

            # 이동하는 말 위에 있는 말들은 다 같이 움직여야 함. 현재 조사중인 말의 인덱스 찾기
            # 가장 아랫쪽에 있는 말만 이동할 수 있음 -> index가 0이 아닐 경우 continue
            if (piece_pos[r][c].index(p.idx)):
                continue

            match (nextPosColor):
                case 2:
                    # 파란색 칸의 경우 말의 이동 방향을 반대로 한 후 이동
                    p.dir = (1, 0, 3, 2)[p.dir]  # 우 좌 상 하
                    nr, nc = map(operator.add, p.pos, direction_delta[p.dir])  # 다음 이동할 칸

                    # 방향을 바꾼 후 이동하려는 칸이 파란 색이 아닌 경우에만 이동
                    nextPosColor = board[nr][nc] if 0 <= nr < N and 0 <= nc < N else 2
                    match (nextPosColor):
                        case 2:
                            continue # 방향을 바꿨는데 다음 칸이 또 파란 칸이거나 board를 벗어나는 경우
                        case x:
                            move((r, c), (nr, nc), case=x)
                case x:  # 흰 칸이나 빨간 칸의 경우
                    move((r, c), (nr, nc), case=x)
            
            # 종료조건: 특정 칸에 쌓인 말의 개수가 4개 이상인 경우
            if (len(piece_pos[nr][nc]) >= 4):
                return cnt+1
    
    return -1

print(simulation())
