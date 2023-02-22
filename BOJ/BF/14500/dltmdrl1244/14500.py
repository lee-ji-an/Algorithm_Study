import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
maxans = 0

tetrominos = [
    [(1, 0), (2, 0), (3, 0)], # ㅣ 모양
    [(0, 1), (0, 2), (0, 3)],
    
    [(0, 1), (1, 0), (1, 1)], # ㅁ 모양
    
    [(1, -1), (1, 0), (1, 1)], # ㅗ 모양
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (2, 0)],
    [(1, 0), (1, 1), (2, 0)],
    
    [(1, 0), (1, 1), (1, 2)], # ㄴ 모양
    [(1, 0), (2, 0), (2, -1)],
    [(-1, -2), (-1, -1), (-1, 0)],
    [(0, 1), (1, 0), (2, 0)],
    
    [(1, -2), (1, -1), (1, 0)], # 리버스 ㄴ 모양
    [(0, 1), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (0, 2)],
    [(1, 0), (2, 0), (2, 1)],
    
    [(0, 1), (1, 0), (1, -1)], # 번개모양1
    [(1, 0), (1, 1), (2, 1)],
    
    [(0, 1), (1, 1), (1, 2)], # 번개모양2
    [(1, -1), (1, 0), (2, -1)]    
]

def solve(y, x):
    global maxans
    # 각 칸에 대해 모든 테트로미노 고려
    for tetromino in tetrominos:
        s = board[y][x]
        for offset in tetromino:
            ny, nx = y + offset[0], x + offset[1]
            
            if 0 <= ny < n and 0 <= nx < m:
                s += board[ny][nx]
            # 범위 벗어나면 즉시 종료
            else:
                break
        
        maxans = max(maxans, s)
            

for i in range(n):
    for j in range(m):
        solve(i, j)

print(maxans)