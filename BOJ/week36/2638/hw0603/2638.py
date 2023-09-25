from collections import deque, Counter
from itertools import chain
import sys

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, sys.stdin.readline().strip().split())
matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# (0, 0)을 기준으로 치즈 외부 공간을 별도로 마킹
q = deque([(0, 0)])
matrix[0][0] = 9
visited[0][0] = True

while (q):
    row, col = q.popleft()

    for i in range(4):
        nr, nc = row+dr[i], col+dc[i]
        
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if (visited[nr][nc]):
            continue
        if (matrix[nr][nc] == 1):
            continue

        matrix[nr][nc] = 9  # 치즈 외부 공간 마킹
        visited[nr][nc] = True
        q.append((nr, nc))

# print("----초기----")
# print(*matrix, sep='\n')
# print()

def spread(row, col):
    global matrix
    visited = set()
    visited.add((row, col))

    q = deque([(row, col)])
    while (q):
        r, c  = q.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if ((nr, nc) in visited):
                continue
            visited.add((nr, nc))
            if (matrix[nr][nc] == 0):
                matrix[nr][nc] = 9  # 외부공기 들어옴
                q.append((nr, nc))

def removeCheese(row, col):
    global cheeseCnt, visited, matrix

    visited[row][col] = True
    q = deque([(row, col)])
    melting_q = deque()

    while (q):
        row, col = q.popleft()
        adjCnt = 0
        for i in range(4):
            nr, nc = row+dr[i], col+dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if (matrix[nr][nc] == 9 and matrix[row][col] == 1):
                adjCnt += 1
            if (visited[nr][nc]):
                continue
            visited[nr][nc] = True
            q.append((nr, nc))
        
        if (adjCnt >= 2):
            matrix[row][col] = 'C'
            melting_q.append((row, col))
    
    # print(*matrix, sep='\n')
    # print(f"{day+1}일차에 {len(melting_q)}개 녹음")
    tmp = set()
    while (melting_q):
        row, col = melting_q.popleft()
        matrix[row][col] = 9
        spread(row, col)
        cheeseCnt -= 1

# 시간의 흐름에 따른 치즈 시뮬레이션 -> 치즈 개수가 0이 될 때 까지
day = 0
cheeseCnt = Counter(chain.from_iterable(matrix)).get(1)  # 초기 치즈 개수
while (cheeseCnt > 0):
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if (not visited[i][j] and matrix[i][j] == 1):
                removeCheese(i, j)
                day += 1
                # print(f"----{day}일 경과 후----")
                # print(*matrix, sep='\n')
                # print()

print(day)
