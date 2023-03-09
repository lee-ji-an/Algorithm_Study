import sys
from collections import deque


def sol():
    while coordinate:
        y, x = coordinate.popleft()
        if (y, x) not in candidate_dict:        # 해당 좌표에서 후보자들을 뽑음
            candidate = check_area(y, x)
            candidate = check_col(candidate, y, x)
            candidate = check_row(candidate, y, x)
            candidate_dict[(y, x)] = candidate
        candidate = candidate_dict[(y, x)]      # 기존에 후보자가 있다면 그것을 사용함
        for i in candidate:
            if i > maps[y][x]:      # 이미 탐색했던 값임
                maps[y][x] = i
                before.append((y, x))       # 값이 할당된 좌표는 before로 넘어감
                break
        else:
            coordinate.appendleft((y, x))       # 만약 가능한 값이 없다면 복구함
            maps[y][x] = 0      # 값도 초기화함
            candidate_dict.pop((y, x))      # 해당 좌표에서 후보자는 다시 찾아야하므로 초기화
            coordinate.appendleft(before.pop())     # 앞에서 할당된 애도 다시 후보자로 넣음
    for m in maps:
        print(*m, sep=' ')


def check_area(y, x):
    # 3 * 3 구역을 체크함
    c_y = (y // 3) * 3
    c_x = (x // 3) * 3
    candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(c_y, c_y + 3):
        for j in range(c_x, c_x + 3):
            if maps[i][j] in candidate:
                candidate.remove(maps[i][j])
    # print(candidate)
    return candidate


def check_col(candidate, y, x):
    # 열을 체크함
    for m in maps:
        if m[x] in candidate:
            candidate.remove(m[x])
    return candidate


def check_row(candidate, y, x):
    # 행을 체크함
    for m in maps[y]:
        if m in candidate:
            candidate.remove(m)
    return candidate


if __name__ == "__main__":
    maps = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
    coordinate = deque()        # 들어가야 하는 좌표들
    before = deque()        # 이미 값이 할당되었던 좌표들
    for i in range(9):
        for j in range(9):
            if maps[i][j] == 0:
                coordinate.append((i, j))
                # 0의 좌표를 찾음
    candidate_dict = dict()
    sol()