import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def bfs(sy, sx):
    q = deque([(sy, sx)])
    visited = [[False for _ in range(m)] for _ in range(n+1)]
    visited[sy][sx] = True
    delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    candidate = []

    while q:
        for _ in range(len(q)):
            cy, cx = q.popleft()
            for i in range(4):
                ny, nx = cy + delta[i][0], cx + delta[i][1]

                if not (0 <= ny < n and 0 <= nx < m):
                    continue

                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

                if board_copy[ny][nx] == 1:
                    candidate.append(((ny, nx)))

        # 찾은 적이 하나라도 있으면 break
        if candidate:
            break
    
    # 가장 왼쪽에 있는 것이 처음에 오도록 정렬 (x좌표 오름차순)
    if candidate:
        candidate.sort(key= lambda x: (x[1]))
        return candidate[0]
    
    # 만약 찾은 적이 없다면 -1, -1 리턴하여 종료
    return -1, -1


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
# 총 적의 수
enemy = sum(sum(board[i]) for i in range(n))
ans = -1

# 조합을 이용해서 궁수를 배치하는 경우의 수 순회
for archers in combinations([i for i in range(m)], 3):
    board_copy = [board[i][:] for i in range(n)]
    cur_enemy = enemy
    score = 0
    
    while cur_enemy:
        bottom_level = sum(board_copy[n-1])
        victim = []

        # 각 궁수별로 쏠 적을 찾는다.
        for ax in archers:
            ey, ex = bfs(n, ax)

            if (ey, ex) != (-1, -1) and (ey, ex) not in victim:
                victim.append((ey, ex))
            
        # 적을 처치하고 점수 올림
        for vy, vx in victim:
            score += 1
            board_copy[vy][vx] = 0

            if vy != n-1:
                cur_enemy -= 1

        # 적 수를 감소, 한 칸 전진
        cur_enemy -= bottom_level
        board_copy.pop()
        board_copy.insert(0, [0 for _ in range(m)])

    ans = max(ans, score)

print(ans)