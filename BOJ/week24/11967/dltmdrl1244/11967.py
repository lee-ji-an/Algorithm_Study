import sys
from collections import deque
input = sys.stdin.readline

'''
어떤 갈수있는 방에 인접한 방들은 두가지 경우
1) 불이 켜져있어 바로 갈 수 있는 경우
2) 불이 꺼져있어 바로는 갈 수 없는 경우

1)의 경우 바로 큐에 넣는다
2)의 경우 nolight 셋에 넣는다.
    다른 곳을 탐색하다가 그 곳을 켤 수 있는 불이 있으면 (인접한 방이 nolight 안에 있으면)
    큐에 넣는다
'''

n, m = map(int, input().split())
light = dict()
visited = [[False for _ in range(n+1)] for _ in range(n+1)]
lighton = set()
nolight = set()
ans = 1

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(m):
    x, y, a, b = map(int, input().split())
    if (x, y) in light:
        light[(x, y)].append((a, b))
    else:
        light[(x, y)] = [(a, b)]


q = deque()
q.append((1, 1))
lighton.add((1, 1))

while q:
    cy, cx = q.popleft()
    visited[cy][cx] = True

    # 현재 방에서 켤 수 있는 스위치를 모두 켠다.
    # 이 때 전에 길은 있으나 불이 꺼져있어 못 갔었던 방이 있다면 그 방은 이제 갈수 있게 됐으므로 큐에 넣는다.
    if (cy, cx) in light:
        for l in light[(cy, cx)]:
            if l in nolight:
                q.append(l)
                nolight.remove(l)

            lighton.add(l)
    
    # 인접한 방 탐색
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0 < ny <= n and 0 < nx <= n:
            # 만약 불이 켜져 있다면 ((ny, nx)가 lighton에 있다면) 바로 갈 수 있다
            if not visited[ny][nx]:
                if (ny, nx) in lighton:
                    q.append((ny, nx))
                # 그렇지 않으면 일단 nolight에 넣는다
                else:
                    nolight.add((ny, nx))

# 불이 켜진 방의 개수를 출력
print(len(lighton))