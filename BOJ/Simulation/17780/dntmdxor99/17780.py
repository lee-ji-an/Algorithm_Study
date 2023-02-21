from collections import deque


class Chess:
    def __init__(self, y: int, x: int, dir: int):
        self.y, self.x = y - 1, x - 1
        if dir == 1: self.dy, self.dx = 0, 1  # 우측
        elif dir == 2: self.dy, self.dx = 0, -1  # 좌측
        elif dir == 3: self.dy, self.dx = -1, 0  # 상단
        elif dir == 4: self.dy, self.dx = 1, 0  # 하단

    def move(self, dy: int, dx: int):  # 이동하는 함수, 맨 아래에 있는 말의 방향으로 움직임
        self.y, self.x = self.y + dy, self.x + dx

    def expect_move(self):      # 다음 위치를 예상하는 함수
        return self.y + self.dy, self.x + self.dx

    def chdir(self):  # 방향을 바꿈
        if self.dy != 0: self.dy = -1 if self.dy == 1 else 1
        elif self.dx != 0: self.dx = -1 if self.dx == 1 else 1


def move(y, x, dy, dx, flag=1):
    ny, nx = y + dy, x + dx
    while mv_maps[y][x]:
        i = mv_maps[y][x].popleft() if flag else mv_maps[y][x].pop()  # 하나씩 빼서 움직임, 아래에서부터
        i.move(dy, dx)  # 움직임
        mv_maps[ny][nx].append(i)


def switch(inst):
    ny, nx = inst.expect_move()
    if 0 <= ny < n and 0 <= nx < n:
        if maps[ny][nx] == 0:  # 다 같이 움직이면 됨
            move(inst.y, inst.x, inst.dy, inst.dx, 1)
        elif maps[ny][nx] == 1:  # 움직이되, 순서를 바꿈
            move(inst.y, inst.x, inst.dy, inst.dx, 0)
        elif maps[ny][nx] == 2:
            inst.chdir()
            return 1        # 파란색을 만났으므로, 방향을 변경함
    else:       # 범위를 벗어났음
        inst.chdir()
        switch(inst)
    return 0


if __name__ == "__main__":
    n, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    mv_maps = [[deque() for _ in range(n)] for _ in range(n)]
    inst_list = []
    for _ in range(k):
        tmp = Chess(*map(int, input().split()))
        inst_list.append(tmp)
        mv_maps[tmp.y][tmp.x].append(tmp)

    for idx in range(1, 1001):
        for inst in inst_list:
            if mv_maps[inst.y][inst.x][0] == inst:  # 만약 제일 아래에 있는 말이라면
                if switch(inst):        # 파란색을 만났음
                    switch(inst)
            if len(mv_maps[inst.y][inst.x]) >= 4:
                print(idx)
                exit(0)
    print(-1)
