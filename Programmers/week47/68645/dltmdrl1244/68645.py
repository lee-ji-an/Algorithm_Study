import sys
input = sys.stdin.readline

def move1(y, x):
    global num
    flag = False

    for _ in range(n):
        if y >= n or board[y][x] != 0:
            break
        flag = True
        board[y][x] = num
        y += 1
        num += 1

    y -= 1
    return y, x, flag

def move2(y, x):
    global num
    flag = False

    for _ in range(n):
        if x > y or board[y][x] != 0:
            break
        flag = True
        board[y][x] = num
        x += 1
        num += 1

    x -= 1
    return y, x, flag
    
def move3(y, x):
    global num
    flag = False

    for _ in range(n):
        if y <= 0 or x <= 0 or board[y][x] != 0:
            break

        flag = True
        board[y][x] = num
        y -= 1
        x -= 1
        num += 1

    y += 1
    x += 1
    return y, x, flag

n = int(input())
answer = []
board = [[0 for _ in range(i+1)] for i in range(n)]

y, x = 0, 0
num = 1
flag = False

while True:
    flag = False
    y, x, flag = move1(y, x)
    x += 1
    y, x, flag = move2(y, x)
    x -= 1
    y -= 1
    y, x, flag = move3(y, x)
    y += 1

    if not flag:
        break

print(*board, sep="\n")

for b in board:
    answer += b
