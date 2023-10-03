import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    maps = [[-1] * n for _ in range(n)]
    maps[0][0] = 1      # snake

    k = int(input())
    for _ in range(k):
        y, x = map(int, input().split())
        maps[y - 1][x - 1] = 0      # 사과가 있음

    move = dict()
    l = int(input())
    for _ in range(l):
        sec, dir = input().split()
        move[int(sec)] = 1 if dir == 'D' else - 1

    tailMove = dict()
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    headDir = 0
    tailDir = 0
    headY, headX = 0, 0
    tailY, tailX = 0, 0

    for sec in range(1, n ** 2):
        headY += dir[headDir][0]
        headX += dir[headDir][1]
        
        if not(0 <= headY < n and 0 <= headX < n):
            break

        headDir = (headDir + move.get(sec, 0)) % 4
        tailMove[(headY, headX)] = move.get(sec, 0)
        flag = maps[headY][headX]
            
        match flag:
            case -1:
                ## no apple, no snake
                maps[headY][headX] = 1      # 이제 뱀이 있음
                maps[tailY][tailX] = -1     # 꼬리 제거

                tailDir = (tailDir + tailMove.get((tailY, tailX), 0)) % 4        # 꼬리가 방향을 전환함
                tailY += dir[tailDir][0]
                tailX += dir[tailDir][1]
            case 0:
                ## apple
                maps[headY][headX] = 1      # 이제 뱀이 있음
            case 1:
                ## snake
                break

    print(sec)