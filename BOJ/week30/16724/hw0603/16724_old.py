import sys

N, M = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().strip()) for _ in range(N)]
sector = [[0]*M for _ in range(N)]  # 0=방문안함, -1=가방문 상태, N=섹터 지정 상태
cnt = 0


def search(row, col):
    global cnt

    # 경로 따라 방문하지 않은 곳을 다 방문하며 경로 저장
    hist = set()
    while not (sector[row][col]):
        sector[row][col] = -1  # 가방문 처리(이번 시행에 방문한 지역이지만, 아직 섹터 확정 X)
        hist.add((row, col))
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
    if (sector[row][col] > 0):
        for r, c in hist:
            sector[r][c] = sector[row][col]
    # 이번 시행에 처음 방문한 경우 -> 새로운 섹터 배정
    else:
        cnt += 1
        for r, c in hist:
            sector[r][c] = cnt


for i in range(N):
    for j in range(M):
        if not (sector[i][j]):
            search(i, j)

print(cnt)
