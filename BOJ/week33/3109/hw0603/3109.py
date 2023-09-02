import sys

R, C = map(int, sys.stdin.readline().strip().split())
matrix = [list(sys.stdin.readline().strip()) for _ in range(R)]

# 함수로 처리하면 시간초과 남..
# def checkRange(row, col):
#     return (0 <= row < R and 0 <= col < C)


def dfs(origin, row, col) -> bool:
    # 목적지 도착 시 True 반환
    if (col == C-1):
        # matrix[row][col] = str(origin)
        return True

    # 오른쪽 대각선 위
    nr, nc = row-1, col+1
    if (0 <= nr < R and matrix[nr][nc] == '.'):
        matrix[nr][nc] = 'o'
        if (dfs(origin, nr, nc)):
            return True
    # 오른쪽
    nr, nc = row, col+1
    if (0 <= nr < R and matrix[nr][nc] == '.'):
        matrix[nr][nc] = 'o'  # str(origin) 하면 메모리 엄청 씀..?
        if (dfs(origin, nr, nc)):
            return True
    # 오른쪽 대각선 아래
    nr, nc = row+1, col+1
    if (0 <= nr < R and matrix[nr][nc] == '.'):
        matrix[nr][nc] = 'o'
        if (dfs(origin, nr, nc)):
            return True

    return False


print(sum(dfs(r, r, 0) for r in range(R)))
# print(*matrix, sep='\n')
