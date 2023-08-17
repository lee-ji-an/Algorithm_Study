import sys
input = sys.stdin.readline

def all(y, x, offset):
    for i in range(y, y + offset):
        for j in range(x, x + offset):
            if maps[i][j] == 0:
                return False
    return True


def any(y):
    for i in range(10):
        if maps[y][i]:
            return True      
    return False


def conv(maps, y, nextX, cnt):
    global ans

    if ans < cnt:
        return
    
    elif nextX >= 10:
        return
    
    elif y == 10 and not any(9):
        ans = cnt
        return
    
    else:
        if candidate[y]:
            for x in range(nextX, 10):
                if x in candidate[y]:
                    for i in range(min(5, 10 - y, 10 - x), 0, -1):
                        if candidateNum[i] <= 4:
                            if maps[y][x] and maps[y][x + i - 1] and maps[y + i - 1][x] and maps[y + i - 1][x + i - 1]:
                                # if all(sum([maps[row][x : x + i] for row in range(y, y + i)], [])):
                                if all(y, x, i):
                                    candidateNum[i] += 1

                                    for row in range(y, y + i):
                                        maps[row][x : x + i] = [0] * i
                                    
                                    if any(y):
                                        conv(maps, y, x + i, cnt + 1)
                                    else:
                                        conv(maps, y + 1, 0 , cnt + 1)

                                    for row in range(y, y + i):
                                        maps[row][x : x + i] = [1] * i

                                    candidateNum[i] -= 1
            if any(y):
                return
            else:
                conv(maps, y + 1, 0, cnt)
        else:
            conv(maps, y + 1, 0, cnt)


if __name__ == "__main__":
    maps = [list(map(int, input().split())) for _ in range(10)]
    candidate = [set() for _ in range(10)]
    candidateNum = [0] * 6
    ans = 26

    for y in range(10):
        for x in range(10):
            if maps[y][x]:
                candidate[y].add(x)

    conv(maps, 0, 0, 0)
    print(ans if ans < 26 else -1)