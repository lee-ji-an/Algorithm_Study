import sys
from collections import deque
input = sys.stdin.readline

# 사다리 n 뱀 m
n, m = map(int, input().split())
# 사다리와 뱀을 딕셔너리에 저장. dic[출발] = 도착 형식으로 저장하여 키값에서 밸류값을 쉽게 찾도록 함
ladder = {}
snake = {}
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

def bfs():
    # 1~100
    visited = [False] * 101
    visited[1] = True
    q = deque([(1, 0)])

    while q:
        cur, cnt = q.popleft()
        # 100(목표)에 도착하면 return cnt
        # 문제 조건에 의해 도착할 수 있는 입력만 주어지므로 예외처리 필요 x
        if cur == 100:
            return cnt

        for i in range(1, 7):
            # 100보다 큰 수, 예컨대 99에서 2~6은 101~105이므로 pass
            # 사다리와 뱀의 도착점은 100 이하이므로 고려할 필요 x, 주사위로 인해 100이 넘는 것만 고려
            if cur + i > 100:
                continue

            nxt = cur + i
            # 이동한 칸이 사다리나 뱀의 시작점이면 끝점으로 이동함. 이동 안하는거 불가능 무조건 이동
            if nxt in ladder:
                nxt = ladder[nxt]
            elif nxt in snake:
                nxt = snake[nxt]

            # BFS
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, cnt + 1))

print(bfs())