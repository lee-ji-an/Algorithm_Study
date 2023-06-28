import sys
input = sys.stdin.readline

N, M = map(int, input().split())

paper = []
for i in range(N):
    paper.append(list(map(int, input().rstrip())))
max_ans = 0

# 0 : 세로, 1 : 가로
for i in range(1 << (N * M)):  # ex) N:2, M:2 ==== 0000, 0001, 0010, 0011, 0100, 1001, ...
    total = 0
    # 가로 방향 조각 계산
    for row in range(N):
        row_sum = 0
        for col in range(M):
            idx = row * M + col
            # 가로일 때
            if i & (1 << idx) != 0:
                row_sum = row_sum * 10 + paper[row][col]
            # 세로일 때
            else:
                total += row_sum
                row_sum = 0
        total += row_sum
    # 세로 방향 조각 계산
    for col in range(M):
        col_sum = 0
        for row in range(N):
            idx = row * M + col
            # 세로일 때
            if i & (1 << idx) == 0:
                col_sum = col_sum * 10 + paper[row][col]
            # 가로일 때
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    max_ans = max(max_ans, total)

print(max_ans)
