import sys
input = sys.stdin.readline

def road_check(p1, p2): # 두 지점 간 도로가 있으면 true 없으면 false
    if (p1[0], p1[1], p2[0], p2[1]) in no_road or (p2[0], p2[1], p1[0], p1[1]) in no_road:
        return False
    
    return True

n, m = map(int, input().split())
k = int(input())
board = [[0 for _ in range(m+1)] for _ in range(n+1)]
no_road = set()

for _ in range(k):
    a, b, c, d = map(int, input().split())
    no_road.add((a, b, c, d))

for i in range(m+1):
    # 바운더리 부분에 도로가 끊겨 있으면 그 뒤로는 n+m만에 갈 수 없으므로 0을 기록
    if not road_check((0, i-1), (0, i)):
        break

    board[0][i] = 1

for i in range(n+1):
    if not road_check((i, 0), (i-1, 0)):
        break

    board[i][0] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        # 도로가 끊겨 있지 않다면, 위 또는 왼쪽의 값을 더한다.
        if road_check((i-1, j), (i, j)):
            board[i][j] += board[i-1][j]
        
        if road_check((i, j-1), (i, j)):
            board[i][j] += board[i][j-1]

print(board[n][m])