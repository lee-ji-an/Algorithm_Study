import sys
sys.setrecursionlimit(10**8)

def solution(grid):
    answer = []
    N, M = len(grid), len(grid[0])
    
    dr = (-1, 0, 1, 0)  # 북쪽부터 시계방향
    dc = (0, 1, 0, -1)
    
    def dfs(row, col, dir, hist):
        if ((row, col, dir) in hist):
            return len(hist) - hist.get((row, col, dir))
        
        hist[(row, col, dir)] = len(hist)
        
        nodeType = grid[row][col]
        if (nodeType == 'S'):
            nd = dir % 4
        elif (nodeType == 'L'):
            nd = (dir-1) % 4
        elif (nodeType == 'R'):
            nd = (dir+1) % 4
        nr, nc = (row+dr[nd])%N, (col+dc[nd])%M
        
        checked.add((nr, nc, nd))
        # print((nr, nc, nd, hist))
        return dfs(nr, nc, nd, hist)
    
    checked = set()
    for i in range(N):
        for j in range(M):
            for dir in range(4):
                if ((i, j, dir) in checked):
                    continue
                checked.add((i, j, dir))
                # print((i, j, dir, dict()))
                result = dfs(i, j, dir, dict())
                answer.append(result)
                # print("----")
                
    
    return sorted(answer)