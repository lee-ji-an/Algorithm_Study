import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
isFound = False

def dfs(row: int, col: int, type: str, hist: set, initpos: tuple):
    global isFound
    # 이미 사이클을 찾은 경우 return
    if (isFound):
        return True

    # 사이클이 만들어진 경우 True
    if (initpos == (row, col) and len(hist) >= 4):
        isFound = True
        return True

    # 이미 방문한 위치인 경우
    if ((row, col) in hist):
        return False
    
    # board 범위 밖을 벗어난 경우
    if not (0 <= row < N and 0 <= col < M):
        return False
    
    # type mismatch
    if (type != board[row][col]):
        return False

    # hist에 방문 기록 추가
    hist = hist.copy()
    hist.add((row, col))

    # 4방향 DFS 호출
    a = dfs(*(row-1, col), type, hist, initpos) # 상
    b = dfs(*(row+1, col), type, hist, initpos) # 하
    c = dfs(*(row, col+1), type, hist, initpos) # 우
    d = dfs(*(row, col-1), type, hist, initpos) # 좌

    return any((a, b, c, d))

for i in range(N):
    for j in range(M):
        result = dfs(i, j, board[i][j], set(), (i, j))
        if (result):
            print("Yes")
            sys.exit()

print("No")
