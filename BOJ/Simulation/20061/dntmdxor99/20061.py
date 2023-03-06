import sys


def goto_board(*args):
    # 넣을 수 있는 자리를 찾는 함수
    max_cnt = 7
    for i in range(6):
        for val in args:
            if val & 1 << i == 0:       # i번째 자리가 0이라면
                if max_cnt == 7:        # 초기화 이후 값이 들어간 적 없음
                    max_cnt = i     # 해당 자리에 넣을 수 있음
                else:
                    continue
            else:
                max_cnt = 7     # 만약 자리에 블럭이 있다면 초기화함
                break
    return max_cnt


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().strip())
    green = [0] * 4
    blue = [0] * 4
    score = 0
    count = 0

    for _ in range(n):
        t, y, x = map(int, input().split())
        match t:
            # 넣을 수 있는 좌표를 받아서, 해당 비트에 값을 넣음
            case 1:
                # 1 * 1
                n_x = goto_board(green[x])
                n_y = goto_board(blue[y])
                green[x] += 1 << n_x
                blue[y] += 1 << n_y
            case 2:
                # 1 * 2
                n_x = goto_board(green[x], green[x + 1])
                n_y = goto_board(blue[y])
                green[x] += 1 << n_x
                green[x + 1] += 1 << n_x
                blue[y] += 3 << n_y
            case 3:
                # 2 * 1
                n_x = goto_board(green[x])
                n_y = goto_board(blue[y], blue[y + 1])
                green[x] += 3 << n_x
                blue[y] += 1 << n_y
                blue[y + 1] += 1 << n_y

        for color in [green, blue]:
            # 색깔별로 겹치는 행이나 열이 있는지 확인함
            i = 0
            while i <= 6:
                idx = 1 << i
                for block in color:
                    if block & idx != idx:
                        # 만약 0이 들어가있다면, 블럭이 없다는 의미이므로 끝냄
                        break
                else:
                    # 무사히 for loop가 끝나면 겹치는 행이나 열이 있다는 의미임
                    # 행이라고 가정함
                    score += 1
                    for idx in range(4):
                        before = color[idx] >> i << i       # 행의 i번째 이후 비트만 남김
                        after = color[idx] >> (i + 1) << i      # 행의 i번째 이후 비트에서 한 칸 땡기면서, i번째 비트도 삭제함
                        color[idx] = color[idx] ^ before | after        # 그리고 한 칸 당긴 값을 넣음
                    i -= 1
                i += 1

        for color in [green, blue]:
            while max(color) >= 16:
                # 16을 넘기면 연한 곳에 있다는 의미이므로 한 칸씩 당기면 됨
                color[0] >>= 1
                color[1] >>= 1
                color[2] >>= 1
                color[3] >>= 1

    for color in [green, blue]:
        for block in color:
            while block:
                block &= block - 1
                count += 1

    print(score)
    print(count)
