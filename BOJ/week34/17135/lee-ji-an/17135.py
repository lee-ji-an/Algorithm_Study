import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M, D = map(int, input().split())
board = []
for n in range(N):
    board.append(list(map(int, input().split())))


def solve(N, M, D, board):
    # 한 궁수가 게임에서 공격한 적 위치를 반환
    def find_enemy(arrow, board):
        visited = [[False] * M for _ in range(N)]
        candidate = set()
        q = deque([(N, arrow)])
        for _ in range(D):
            for _ in range(len(q)):
                row, col = q.popleft()
                for d in range(4):
                    mv_r, mv_c = row + dr[d], col + dc[d]
                    if not (0 <= mv_r < N) or not (0 <= mv_c < M) or visited[mv_r][mv_c]:
                        continue
                    if board[mv_r][mv_c] == 1:
                        candidate.add((mv_r, mv_c))
                    visited[mv_r][mv_c] = True
                    q.append((mv_r, mv_c))
            if candidate:
                return min(candidate, key=lambda x: x[1])
        return None

    # 모든 궁수 위치에 대해서 게임을 시뮬레이션 하는 함수
    def game_simulation(arrows):
        total_enemy = 0
        new_board = deque([r[:] for r in board])
        for n in range(N):
            # 모든 궁수는 동시에 공격함. 따라서, 같은 적을 공격할 수도 있으므로 set으로 죽은 적을 관리
            enemy = set()
            for arrow in arrows:
                enemy_pos = find_enemy(arrow, new_board)
                if enemy_pos is not None:
                    enemy.add(enemy_pos)
            # 죽은 적의 위치는 격자 상에서 0으로 변환
            for e in enemy:
                new_board[e[0]][e[1]] = 0

            # 적이 아래로 이동
            new_board.pop()
            new_board.appendleft([0] * M)

            total_enemy += len(enemy)
        return total_enemy

    ans = 0
    for combi in combinations(range(M), 3):  # 궁수들의 위치를 조합으로 생성
        total_enemy = game_simulation(combi)
        ans = max(ans, total_enemy)

    return ans


print(solve(N, M, D, board))