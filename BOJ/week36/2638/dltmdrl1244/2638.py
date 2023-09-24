import sys
from collections import deque
input = sys.stdin.readline

# 가장자리에는 치즈가 없다는 문제 조건을 이용해서 (0, 0)을 시작으로 치즈가 없는 곳만 BFS 하여 외부 공간을 구별한다
def find_outside():
    q = deque([(0, 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + d[i][0], cx + d[i][1]

            if not (0 <= ny < n and 0 <= nx < m):
                continue
            
            if board[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

    # 방문처리 된 곳은 치즈 외부의 공간, 그대로 리턴
    return visited


def bfs(outside):
    melting = []

    q = deque([(0, 0)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + d[i][0], cx + d[i][1]

            if not (0 <= ny < n and 0 <= nx < m) or visited[ny][nx]:
                continue
            
            # outside를 이용, 외부와 인접해 있는 변이 몇 개인지 카운트
            if board[ny][nx] == 1:
                t = 0
                for j in range(4):
                    nny, nnx = ny + d[j][0], nx + d[j][1]
                    if 0 <= nny < n and 0 <= nnx < m and outside[nny][nnx]:
                        t += 1
                # 두 개 이상의 변이 맞닿아 있다면 이번 차례에 녹는다
                if t >= 2:
                    melting.append((ny, nx))

            visited[ny][nx] = True
            q.append((ny, nx))

    # 이번 차례에 녹아야 하는 칸들을 담아서 리스트 리턴
    return melting
                 
n, m = map(int, input().split())
board = []
cheese = 0
melted = 0
cnt = 0
d = [(0, -1), (0, 1), (1, 0), (-1, 0)]
for _ in range(n):
    t = list(map(int, input().split()))
    cheese += sum(t)
    board.append(t)


while melted != cheese:
    outside = find_outside()
    # melting : 이번 차례에 녹아야 하는 치즈 칸 리스트
    melting = bfs(outside)

    # 일괄적으로 한번에 녹여준다
    for my, mx in melting:
        board[my][mx] = 0
    
    # 녹은 치즈 개수와 흐른 시간 카운트
    melted += len(melting)
    cnt += 1
    
print(cnt)