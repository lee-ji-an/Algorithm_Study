import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
fert = [list(map(int, input().split())) for _ in range(n)]
board = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(m):
    y, x, age = map(int, input().split())
    trees[y-1][x-1].append(age)

def spring_summer():
    for i in range(n):
        for j in range(n):
            grow = deque()
            dead = 0
            for tree_age in trees[i][j]:
                if board[i][j] >= tree_age:
                    board[i][j] -= tree_age
                    grow.append(tree_age + 1)
                else:
                    dead += tree_age // 2

            board[i][j] += dead
            trees[i][j] = grow

def fall_winter():
    for i in range(n):
        for j in range(n):
            for tree_age in trees[i][j]:
                if tree_age % 5 == 0:
                    for k in range(8):
                        ny = i + dy[k]
                        nx = j + dx[k]

                        if 0 <= ny < n and 0 <= nx < n:
                            trees[ny][nx].appendleft(1)
            board[i][j] += fert[i][j]

for _ in range(k):
    spring_summer()
    fall_winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(trees[i][j])
print(ans)