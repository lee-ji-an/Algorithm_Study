import sys
input = sys.stdin.readline


def solve(total, next):
    global minimum

    if total >= minimum:        # 기존의 최솟값 보다 작으면 패스해야함
        return
    
    if check():
        minimum = total
        return
    else:
        for i in range(next, len(candidate)):
            y, x = candidate[i]
            if maps[y][x] == 0 and maps[y][x + 1] == 0:     # 현재와 오른쪽에 라인이 없어야 함.
                maps[y][x] = 1
                maps[y][x + 1] = -1
                horizonInLine[x][0] += 1
                horizonInLine[x + 1][1] += 1

                solve(total + 1, i + 1)

                maps[y][x] = 0
                maps[y][x + 1] = 0
                horizonInLine[x][0] -= 1
                horizonInLine[x + 1][1] -= 1


def check():
    for x in range(1, n + 1):       # 전체 라인에 대해서 검사해야 함
        if horizonInLine[x][0] % 2 and horizonInLine[x][1] % 2 and ((horizonInLine[x][0] + horizonInLine[x][1]) % 2):
            return False
        else:
            cur = x
            for y in range(1, h + 1):
                if maps[y][cur] == 1:
                    cur += 1
                elif maps[y][cur] == -1:
                    cur -= 1

            if x != cur:        # 라인 하나라도 틀리면 False임
                return False
            
    return True
                

if __name__ == "__main__":
    n, m, h = map(int, input().split())
    maps = [[0] * (n + 1) for _ in range(h + 1)]
    candidate = []
    horizonInLine = [[0, 0] for _ in range(n + 1)]        # 0번째는 오른쪽으로, 1번째는 왼쪽으로 가는 사다리
    minimum = 4

    for _ in range(m):
        y, x = map(int, input().split())
        maps[y][x] = 1      # 오른쪽으로
        maps[y][x + 1] = -1     # 왼쪽으로

        horizonInLine[x][0] += 1
        horizonInLine[x + 1][1] += 1

    for y in range(1, h + 1):
        for x in range(1, n):       # 오른쪽만 볼거임
            if maps[y][x] == 0 and maps[y][x + 1] == 0:        # 오른쪽에 라인이 없어야 함
                candidate.append((y, x))

    solve(0, 0)
    print(minimum if minimum < 4 else -1)
