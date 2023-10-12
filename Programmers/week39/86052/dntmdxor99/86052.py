def solution(grid):
    def rotation(y, x, d):      # 방향 전환을 하는 로직
        if grid[y][x] == 'S':
            return d
        elif grid[y][x] == 'R':
            return (d + 1) % 4
        else:
            return (d - 1) % 4
    
    
    def cycle(y, x, d):
        length = 1      # 일단은 맨 처음 쏴보긴 해야됨.
        check[y][x][d] = True       # 해당 위치에서 해당 방향으로 빛을 쏜 적이 있음
        curY, curX = (y + dir[d][0]) % h, (x + dir[d][1]) % w       # 빛이 한 칸 이동함. 끝이라면 반대로 이동함.
        curD = rotation(curY, curX, d)      # 해당 칸에서 빛이 방향 전환을 함.
        
        while not (curY == y and curX == x and curD == d):      # 모든 값이 같으면 사이클인 것임
            length += 1
            check[curY][curX][curD] = True
            curY, curX = (curY + dir[curD][0]) % h, (curX + dir[curD][1]) % w
            curD = rotation(curY, curX, curD)
        
        return length
    

    answer = []
    
    h = len(grid)
    w = len(grid[0])
    check = [[[False] * 4 for _ in range(w)] for _ in range(h)]     # 특정 좌표에서 특정 방향으로 나간 적 있는지
    dir = {0 : [-1, 0], 1 : [0, 1], 2 : [1, 0], 3 : [0, -1]}
    
    for i in range(h):
        for j in range(w):
            for d in range(4):
                if not check[i][j][d]:      # 해당 방향으로 빛을 내보낸 적이 없다면
                    answer.append(cycle(i, j, d))
    
    answer.sort()       # 정렬
    return answer