import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[None]*M for _ in range(N)]  # None: 초기상태, signature: 방문후 대표값 지정상태
cnt = 0

sectorData = {}

def search(row, col, signature):
    global cnt

    while not (visited[row][col]):
        visited[row][col] = signature
        match (matrix[row][col]):
            case 'U':
                row -= 1
            case 'D':
                row += 1
            case 'R':
                col += 1
            case 'L':
                col -= 1
    
    # 이전 sector에 포함된 영역을 재방문한 경우 -> 해당 섹터로 편입
    if (past := sectorData.get(visited[row][col], None)):
        sectorData[signature] = past
    # 이번 시행에 처음 방문한 경우 -> 새로운 섹터 배정
    else:
        cnt += 1
        sectorData[signature] = cnt


for i in range(N):
    for j in range(M):
        if not (visited[i][j]):
            search(i, j, signature=(i, j))  # 시그니처를 잘 잡아야..

print(cnt)