from itertools import combinations
from collections import deque
import sys

dr = (0, -1, 0, 1)
dc = (-1, 0, 1, 0)

N, M, D = map(int, sys.stdin.readline().split())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] + [[0]*M]
enemies = set()

for i in range(N):
    for j in range(M):
        if (space[i][j]):
            enemies.add((i, j))

def simulation(archer_pos: tuple, enemie_pos: set) -> int:
    def attack(archer_pos: tuple, enemie_pos: set) -> int:
        candidate = []
        for archer in archer_pos:
            visited = set()
            visited.add((N, archer))
            q = deque([(N, archer)])
            d = 0
            while (q):
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for i in range(4):
                        nr, nc = row+dr[i], col+dc[i]
                        if not (0 <= nr < N and 0 <= nc < M):
                            continue
                        if ((nr, nc) in visited):
                            continue
                        if ((nr, nc) in enemie_pos):
                            candidate.append((nr, nc))
                            q.clear()
                            break
                        visited.add((nr, nc))
                        q.append((nr, nc))
                    if not (q):
                        break
                d += 1
                if (d >= D):
                    break
        
        for e in set(candidate):
            enemie_pos.remove(e)
        
        return len(set(candidate))  # 제거한 적의 수

    
    def move_down(enemie_pos) -> set:
        temp = set()
        
        for row, col in enemie_pos:
            if not (row+1 < N):
                continue
            temp.add((row+1, col))
        
        return temp
    
    # 0. 궁수 좌표 마킹
    archer = [0]*M
    for p in archer_pos:
        archer[p] = 2
    space[N] = archer

    attack_cnt = 0
    while (enemie_pos):
        # 1. 궁수가 거리가 D 이하인 적 중 가장 가까운 적을 제거
        attack_cnt += attack(archer_pos, enemie_pos)
        
        # 2. 적이 아래로 한 칸 이동
        enemie_pos = move_down(enemie_pos)
    
    return attack_cnt


result = 0
for archer_pos in combinations(range(M), 3):
    result = max(result, simulation(archer_pos, enemies.copy()))

print(result)
