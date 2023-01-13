import sys
from itertools import product
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
max_val = float('-inf')

def up(t):
    for i in range(n):
        for j in range(n-1):
            # j 이후 처음으로 0이 아닌 값을 찾음. 위로 미는 것이므로 위에서부터 찾음
            if t[j][i] != 0:
                k = j+1
                while k < n-1 and t[k][i] == 0:
                    k += 1
                # 만약 그 값이 [j][i]와 같다면 합침
                if t[k][i] == t[j][i]:
                    t[j][i] += t[k][i]
                    t[k][i] = 0

        # 띄엄띄엄 존재하는 값들을 한쪽으로 미는 작업
        for j in range(n):
            a = j
            while a > 0 and (t[a][i] != 0 and t[a-1][i] == 0):
                t[a-1][i], t[a][i] = t[a][i], t[a-1][i]
                a -= 1
    return t

def down(t):
    for i in range(n):
        for j in range(n-1, 0, -1):
            # up과 동일, 아래로 미는 것이므로 아래에서부터 찾음
            if t[j][i] != 0:

                k = j-1
                while k > 0 and t[k][i] == 0:
                    k -= 1

                if t[k][i] == t[j][i]:
                    t[j][i] += t[k][i]
                    t[k][i] = 0

        for j in range(n-1, -1, -1):
            a = j
            while a < n-1 and (t[a][i] != 0 and t[a+1][i] == 0):
                t[a+1][i], t[a][i] = t[a][i], t[a+1][i]
                a += 1
    return t

def left(t):
    for i in range(n):
        for j in range(n-1):
            if t[i][j] != 0:

                k = j+1
                while k < n-1 and t[i][k] == 0:
                    k += 1

                if t[i][j] == t[i][k]:
                    t[i][j] += t[i][k]
                    t[i][k] = 0

        for j in range(n):
            a = j
            while a > 0 and (t[i][a] != 0 and t[i][a-1] == 0):
                t[i][a], t[i][a-1] = t[i][a-1], t[i][a]
                a -= 1
    return t

def right(t):
    for i in range(n):
        for j in range(n-1, 0, -1):
            if t[i][j] != 0:

                k = j-1
                while k > 0 and t[i][k] == 0:
                    k -= 1

                if t[i][j] == t[i][k]:
                    t[i][j] += t[i][k]
                    t[i][k] = 0

        for j in range(n-1, -1, -1):
            a = j
            while a < n-1 and (t[i][a] != 0 and t[i][a+1] == 0):
                t[i][a], t[i][a+1] = t[i][a+1], t[i][a]
                a += 1
    return t

# 1234 = 상하좌우
for prod in product([1, 2, 3, 4], repeat=5): # 중복순열 생성
    t = [b[:] for b in board]
    for p in prod:
        if p == 1:
            t = up(t)
        elif p == 2:
            t = down(t)
        elif p == 3:
            t = left(t)
        else:
            t = right(t)

    for i in range(n):
        for j in range(n):
            if t[i][j] != 0:
                max_val = max(max_val, t[i][j])

print(max_val)