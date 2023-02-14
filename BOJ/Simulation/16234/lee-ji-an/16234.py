import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
population = []
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
visited_origin = [[False] * N for _ in range(N)]
dest_q = deque()
day = 0

for i in range(N):
    row_list = list(map(int, input().split()))
    population.append(row_list)
    for j in range(N):
        dest_q.append((i, j))


def bfs(row, col, day):
    q = deque()
    q.append((row, col))
    total_popul = population[row][col]
    union_cnt = 1
    union = [(row, col)]
    visited[row][col] = day
    while q:
        y, x = q.popleft()
        for i in range(4):
            movey = y + dy[i]
            movex = x + dx[i]
            if not(0 <= movey < N) or not(0 <= movex < N):
                continue
            if visited[movey][movex] >= day:
                continue
            if L <= abs(population[y][x] - population[movey][movex]) <= R:
                visited[movey][movex] = day
                q.append((movey, movex))
                total_popul += population[movey][movex]
                union_cnt += 1
                union.append((movey, movex))

    return total_popul // union_cnt, union


def update_popul(avg, union):
    for country in union:
        population[country[0]][country[1]] = avg
        dest_q.append((country[0], country[1]))


visited = [[-1] * N for _ in range(N)]
while dest_q:
    size = len(dest_q)
    for _ in range(size):
        y, x = dest_q.popleft()
        if visited[y][x] < day:
            avg, union = bfs(y, x, day)
            if len(union) <= 1:
                continue
            update_popul(avg, union)
    day += 1


print(day-1)
