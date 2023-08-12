import sys

matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(10)]

def findPoint(matrix) -> tuple:
    # 1. marked 되지 않은 첫 번째 좌표를 찾음
    for i in range(10):
        for j in range(10):
            if (matrix[i][j] == 1):
                return (i, j)
    
    return (-1, -1)

def dfs(matrix: list[list[int]], remain: tuple):
    # 1. marked 되지 않은 첫 번째 좌표를 찾음
    row, col = findPoint(matrix)
    if ((row, col) == (-1, -1)):
        return sum(remain)  # 남은 색종이 수의 합 반환

    # 2. 5가지 색종이에 대해 탐색
    child_results = []
    
    # # 2-1) 1x1 색종이
    # if (remain[0] > 0):
    #     matrixCopy = [r[:] for r in matrix]
    #     data = list(remain)
    #     data[0] -= 1
    #     data = tuple(data)
    #     matrixCopy[row][col] = 9  # 가려진 것으로 마킹
    #     child_results.append(dfs(matrixCopy, remain=data))
    
    # 1x1 색종이 ~ 5x5 색종이
    for k in range(1, 6): # KxK 색종이
        isAllCovered = True
        if (remain[k-1] > 0 and row < 10-k+1 and col < 10-k+1):
            matrixCopy = [r[:] for r in matrix]
            data = list(remain); data[k-1] -= 1; data = tuple(data)

            # isAllCovered = True
            for i in range(row, row+k):
                for j in range(col, col+k):
                    if (matrixCopy[i][j] != 1):
                        isAllCovered = False
                        break
                    else:
                        matrixCopy[i][j] = 9
                if not (isAllCovered):
                    break
            else:
                child_results.append(dfs(matrixCopy, remain=data))
        
        if not (isAllCovered):
            break

    result = max(child_results) if child_results else -sys.maxsize

    return result

ans = dfs(matrix.copy(), (5, 5, 5, 5, 5))
print(25-ans if ans >= 0 else -1)

# print(*matrix, sep='\n')