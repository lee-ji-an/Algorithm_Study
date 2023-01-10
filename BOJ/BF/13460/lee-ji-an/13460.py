import sys

def move(rx, ry, bx, by, d):
    dirx = dx[d]
    diry = dy[d]
    flagr = False
    flagb = False
    while True:
        initrx = rx
        initry = ry
        initbx = bx
        initby = by
        while True:
            rx = rx + dirx
            ry = ry + diry
            if board[ry][rx] == 'O':  # 구멍에 빠졌는지 먼저 겁사해야 함 (바로 아래 if문과 순서 바뀌면 안됨)
                flagr = True
                break
            if board[ry][rx] == '#' or (rx == bx and ry == by):
                rx = rx - dirx
                ry = ry - diry
                break

        while True:
            bx = bx + dirx
            by = by + diry
            if board[by][bx] == 'O':
                flagb = True
                break
            if board[by][bx] == '#' or (rx == bx and ry == by):
                bx = bx - dirx
                by = by - diry
                break

        if flagr or flagb:
            return rx, ry, bx, by, flagr, flagb
        if initrx == rx and initry == ry and initbx == bx and initby == by:
            return rx, ry, bx, by, flagr, flagb


def bfs():
    global cnt, top
    while (True):
        if top+1 == len(queue) or cnt == 10:
            return -1
        top += 1
        rx, ry, bx, by, cnt, before = queue[top]
        for idx in range(4):
            if before == idx:
                continue
            elif before == 0 or before == 2:
                if idx == before+1:
                    continue
            elif before == 1 or before == 3:
                if idx == before-1:
                    continue
            drx, dry, dbx, dby, r, b = move(rx, ry, bx, by, idx)
            if r:
                if b:
                    continue
                else:
                    return cnt + 1
            if b:
                continue
            if drx == rx and dry == ry and dbx == bx and dby == by:
                continue
            queue.append((drx, dry, dbx, dby, cnt+1, idx))

inputs = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, inputs().split())
board = []
for i in range(n):
    temp = inputs().strip()
    board.append(temp)
    if "R" in temp:
        rx = temp.find("R")
        ry = i
    if "B" in temp:
        bx = temp.find("B")
        by = i

dir = 0
temp = 0
queue = []
top = -1
cnt = 0
for i in range(4):
    drx, dry, dbx, dby, r, b = move(rx, ry, bx, by, i)
    if r:  # 파란 구슬 혹은 빨간 구슬이 빠졌는지 검사
        if b:
            continue
        else:
            cnt = 1
    if b:
        continue
    if drx == rx and dry == ry and dbx == bx and dby == by:
        continue
    queue.append((drx, dry, dbx, dby, 1, i))
if cnt == 1:
    print(cnt)
else:
    print(bfs())