import heapq
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [['']*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
flower = (-1, -1)
start = (-1, -1)
garbage_pos = []

global dr, dc
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)

# 맵 정보 입력받음
for i in range(N):
    line = sys.stdin.readline().strip()
    for j, data in enumerate(line):
        graph[i][j] = data
        match (data):
            case 'g':
                garbage_pos.append((i, j))
            case 'F':
                flower = (i, j)
            case 'S':
                start = (i, j)

# 맵 전처리: 빈 칸 중 쓰레기 주변의 칸들은 모두 쓰레기 인접 칸으로 마킹
for row, col in garbage_pos:
    for _dr, _dc in {(0, 1), (1, 0), (-1, 0), (0, -1)}:
        nrow, ncol = row+_dr, col+_dc
        if not ((0 <= nrow < N and 0 <= ncol < M)):
            continue  # 맵 범위 밖 Skip
        if ((nrow, ncol) in {flower, start}):
            continue  # 시작지점, 종료지점 Skip
        if (graph[nrow][ncol] == 'g'):
            continue  # 이미 쓰레기가 있는 지점 Skip
        graph[nrow][ncol] = 'a'

# print(*graph, sep='\n')

q = [(0, 0, *start)]  # pass_cnt, adj_cnt, row, col
visited[start[0]][start[1]] = True  # 시작지점 방문처리

while (q):
    pass_cnt, adj_cnt, row, col = heapq.heappop(q)

    for i in range(4):
        nrow, ncol = row+dr[i], col+dc[i]
        
        # 도착지점 도착한 경우
        if ((nrow, ncol) == flower):
            sys.exit(print(pass_cnt, adj_cnt))

        if not (0 <= nrow < N and 0 <= ncol < M):
            continue  # 범위 밖 Skip
        if (visited[nrow][ncol]):
            continue  # 이미 방문한 곳 Skip

        visited[nrow][ncol] = True  # 좌표 방문처리 
        
        match (graph[nrow][ncol]):
            case '.':
                heapq.heappush(q, (pass_cnt, adj_cnt, nrow, ncol))  
            case 'a':
                heapq.heappush(q, (pass_cnt, adj_cnt+1, nrow, ncol))
            case 'g':
                heapq.heappush(q, (pass_cnt+1, adj_cnt, nrow, ncol))
