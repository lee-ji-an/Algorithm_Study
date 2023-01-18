from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
ladder = {
    k: v for k, v in (
        map(int, sys.stdin.readline().split()) for _ in range(N)
    )
}
snake = {
    k: v for k, v in (
        map(int, sys.stdin.readline().split()) for _ in range(M)
    )
}
visited = set()

# 1번 칸부터 시작
q = deque([(1, 0)]) # (pos, cnt)
# BFS
while (q):
    pos, cnt = q.popleft()

    # 주사위 굴림
    for dice in range(1, 7):
        dest = jump if (jump := ladder.get(pos+dice)) else fall if (fall := snake.get(pos+dice)) else pos+dice

        if (dest == 100):
            print(cnt+1)
            q.clear()
            break

        if (dest not in visited and dest < 100):
            visited.add(dest)
            q.append((dest, cnt+1))

#7 - 50 사다리, 55 - 45 뱀, 47 - 94 사다리 이런 식으로 연결 될 경우도 있기 반드시 뱀도 포함하여 최단 거리를 계산해야 됨
