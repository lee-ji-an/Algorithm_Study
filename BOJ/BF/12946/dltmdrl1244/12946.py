import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
blanks = []
for i in range(n):
    tmp = list(input().rstrip())
    for t in range(n):
        if tmp[t] == 'X':
            blanks.append([i, t])
    board.append(tmp)

color = [[-1] * n for _ in range(n)]
dy = [-1, -1, 0, 0, 1, 1]
dx = [0, 1, -1, 1, -1, 0]
# 빈칸이 아예 없어 답이 0일수도 있으므로 최초 ans는 0
ans = 0

def dfs(y, x, c):
    global ans
    st = deque()
    # 최초 c에는 일단 0번이라는 색깔이 들어있음
    st.append((y, x, c))

    while st:
        cy, cx, cc = st.pop()
        color[cy][cx] = cc
        for i in range(6):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                # [cy][cx]에 인접한 칸 중에 칠해야 할 칸인데 아직 안 칠한 칸이 있으면
                if board[ny][nx] == 'X':
                    if color[ny][nx] == -1:
                        # 답은 최소 2
                        ans = max(ans, 2)
                        # 그리고 현재 [cy][cx]에 칠해진 색과 반대 색깔을 칠한다.
                        if cc == 0:
                            st.append((ny, nx, 1))
                        else:
                            st.append((ny, nx, 0))
                    
                    # 그런데 어떤 인접한 칸의 색깔이 [cy][cx]와 같다면 2개 색깔로 부족하다는 것이므로 답은 3. 즉시 종료
                    elif color[ny][nx] == cc:
                        print(3)
                        exit(0)


for i, j in blanks:
    if color[i][j] == -1:
        # 빈칸 하나라도 있으면 최소 1
        ans = max(1, ans)
        dfs(i, j, 0)

print(ans)