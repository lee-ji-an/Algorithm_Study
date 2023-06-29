import sys

N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
result = 0

# 가로로 이어짐: 1, 세로로 이어짐: 0 -> 사실 별로 중요하지 x. 구분만 해 주면 됨

for bit in range(1 << N*M):  # 0 ~ 2^(N*M)까지 모든 경우의 수 BF
    total = 0
    
    # 가로합 계산
    for row in range(N):
        rowsum = 0
        for col in range(M):
            idx = row*M + col  # board를 1차원 배열로 생각했을 때의 인덱스
            if (bit & (1 << idx)):  # 현재 비트열의 idx 위치에 1이 있으면 가로로 더함
                rowsum = rowsum*10 + board[row][col]
            else:
                total += rowsum
                rowsum = 0
        total += rowsum

    # 세로합 계산
    for col in range(M):
        colsum = 0
        for row in range(N):
            idx = row*M + col  # board를 1차원 배열로 생각했을 때의 인덱스
            if not (bit & (1 << idx)):  # 현재 비트열의 idx 위치에 1이 없다면 세로로 더함
                colsum = colsum*10 + board[row][col]
            else:
                total += colsum
                colsum = 0
        total += colsum
    
    result = max(result, total)  # 최댓값 갱신

print(result)
