import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = []
aircon = []
for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] == -1:
        aircon.append((i, 0))
    board.append(tmp)

def spread():
    dy = [-1, 0, 0, 1]
    dx = [0, 1, -1, 0]
    # 먼지 수가 실시간으로 변하면 확산되는 먼지 수가 달라질 수 있으므로 다른 tmp 배열에 저장
    tmp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                # spread_dust : 확산될 먼지의 양
                spread_dust = board[i][j] // 5
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < n and 0 <= nx < m and board[ny][nx] != -1:
                        # 인접 칸에는 spread_dust 만큼 더해지고, 본 칸에는 spread_dust만큼 빼질 예정
                        tmp[ny][nx] += spread_dust
                        tmp[i][j] -= spread_dust
    # tmp 값을 board에 반영
    for i in range(n):
        for j in range(m):
            board[i][j] += tmp[i][j]
    
def circulate():
    upper, lower = aircon
    
    # 시계방향 회전
    for i in range(upper[0]-1, -1, -1):
        board[i+1][0] = board[i][0]
    # 공기청정기에 들어간 먼지는 0
    board[upper[0]][0] = 0
    for i in range(1, m):
        board[0][i-1] = board[0][i]
    for i in range(1, upper[0]+1):
        board[i-1][m-1] = board[i][m-1]
    for i in range(m-2, -1, -1):
        board[upper[0]][i+1] = board[upper[0]][i]
    
    # 반시계방향 회전
    for i in range(lower[0]+1, n):
        board[i-1][0] = board[i][0]
    # 공기청정기에 들어간 먼지는 0
    board[lower[0]][0] = 0
    for i in range(1, m):
        board[n-1][i-1] = board[n-1][i]
    for i in range(n-2, lower[0]-1, -1):
        board[i+1][m-1] = board[i][m-1]
    for i in range(m-2, -1, -1):
        board[lower[0]][i+1] = board[lower[0]][i]
        
    board[upper[0]][0], board[lower[0]][0] = -1, -1


for _ in range(k):
    spread()
    circulate()

ans = 0
for row in board:
    ans += sum(row)
print(ans + 2)