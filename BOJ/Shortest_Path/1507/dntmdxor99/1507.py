import sys
from itertools import permutations
input = sys.stdin.readline


def sol():
    flag = [[True] * n for _ in range(n)]
    for i, j, k in permutations([*range(n)], 3):
        if maps[i][k] == maps[i][j] + maps[j][k]:
            flag[i][k] = False
        elif maps[i][k] > maps[i][j] + maps[j][k]:
            return -1
    else:
        val = 0
        for i in range(n):
            for j in range(i, n):
                if flag[i][j]:
                    val += maps[i][j]

    return val


if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    print(sol())