import sys
input = sys.stdin.readline

n = int(input())
board = []
bamboo = []
score = [[1 for _ in range(n)] for _ in range(n)]
ans = 1
'''
작은 것에서부터 시작하여, 인근에 나보다 더 큰 칸이 있으면, 즉 자기를 먹을 수 있는 칸을 확인
얘는 나를 먹을 수 있다는 뜻으로 자기가 먹을 수 있는 애보다 + 1개 더 먹을 수 있다.
'''


for i in range(n):
    t = list(map(int, input().split()))
    for j in range(n):
        bamboo.append((t[j], (i, j)))
    board.append(t)

bamboo.sort()

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
for b in bamboo:
    for i in range(4):
        ny = b[1][0] + dy[i]
        nx = b[1][1] + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            if board[ny][nx] > b[0] and score[ny][nx] < score[b[1][0]][b[1][1]] + 1:
                score[ny][nx] = score[b[1][0]][b[1][1]] + 1
                ans = max(ans, score[ny][nx])

print(ans)