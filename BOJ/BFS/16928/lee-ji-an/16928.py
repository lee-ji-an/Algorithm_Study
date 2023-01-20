import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
board = [0 for _ in range(101)]
visited = [0 for _ in range(101)]
q = deque()
for _ in range(N + M):
    start, end = map(int, input().split())
    board[start] = end
def bfs():
    score = 1
    q.append((score, 0))
    visited[score] = 1
    while True:
        score, cnt = q.popleft()
        for i in range(1, 7):
            next_score = score+i   # 주사위 수만큼 이동
            if next_score == 100:
                return cnt+1
            if next_score > 100:
                continue
            if board[next_score] != 0:
                next_score = board[next_score]
            if not visited[next_score]:
                q.append((next_score, cnt+1))
                visited[next_score] = 1

print(bfs())