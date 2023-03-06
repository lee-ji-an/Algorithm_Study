import sys
from collections import deque
m, n, h = map(int, input().split())

boxes = []
unripe = 0
dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()

for i in range(h):
    box = []
    for j in range(n):
        tmp = list(map(int, input().split()))
        for k in range(m):
            if tmp[k] == 1:
                q.append((i, j, k))
        unripe += tmp.count(0)
        box.append(tmp)
    boxes.append(box)

# 이번 회차에서 익은 토마토의 개수를 리턴
def bfs():
    cnt = 0
    # 큐 길이만큼만
    for _ in range(len(q)):
        cz, cy, cx = q.popleft()
        
        for i in range(6):
            nz = cz + dz[i]
            ny = cy + dy[i]
            nx = cx + dx[i]
            
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if boxes[nz][ny][nx] == 0:
                    boxes[nz][ny][nx] = 1
                    cnt += 1
                    q.append((nz, ny, nx))
    
    return cnt


time = 0
while unripe > 0:
    t = bfs()
    # 익은 개수만큼 빼줌
    unripe -= t
    # 이번 회차에 익은 개수가 0이면 이미 전 회차에 다 익었거나, 못 익는 것이 있거나 둘 중 하나
    if t == 0:
        break
    time += 1

# while문 탈출 했는데 안 익은게 있다면 못 익는 것이 있음
if unripe:
    print(-1)
else:
    print(time)