import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
coins = []
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(n):
    tmp = list(input().rstrip())
    for j in range(m):
        # 동전의 정보만 저장
        if tmp[j] == 'o':
            tmp[j] = '.'
            coins.append([i, j])
    board.append(tmp)


# 이동, 만약 떨어진다면 -1, -1 리턴
def move(coinpos, dir):
    ty = coinpos[0] + dy[dir]
    tx = coinpos[1] + dx[dir]
    
    if 0 <= ty < n and 0 <= tx < m:
        # 벽이라면 이동하지 않고, 벽이 아니라면 이동한다.
        if board[ty][tx] != '#':
            return [ty, tx]
        else:
            return coinpos
    # 바운더리를 벗어나면 보드에서 떨어진 것이므로 -1, -1 리턴한다.
    else:
        return -1, -1

def bfs(coins):
    q = deque()
    visited = set()
    q.append(coins)
    visited.add((tuple(coins[0]), tuple(coins[1])))
    cnt = 1
    
    while q:
        # 큐 슬라이싱
        for _ in range(len(q)):
            c1, c2 = q.popleft()
            
            for i in range(4):
                nc1 = move(c1, i)
                nc2 = move(c2, i)
                # 하나만 떨어졌으면 cnt return 
                if (nc1[0] == -1 and nc2[0] != -1) or (nc1[0] != -1 and nc2[0] == -1):
                    return cnt
                
                # 둘 다 떨어졌으면 continue
                if (nc1[0] == -1 and nc2[0] == -1):
                    continue
                
                # 이동한 칸의 정보를 큐에 저장
                if ((tuple(nc1), tuple(nc2))) not in visited:
                    visited.add((tuple(nc1), tuple(nc2)))
                    q.append([nc1, nc2])
        
        cnt += 1
        # 10번만에 성공하지 못하면 -1 return
        if cnt > 10:
            return -1
    return -1


print(bfs(coins))