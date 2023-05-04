import sys
import heapq
input = sys.stdin.readline

ord = {'0':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
       'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}


def my_par(x):
    while x != par[x]:
        x = par[x]
    return x


def union(x, y):
    par_x = my_par(x)
    while y != par[y]:
        temp, y = y, par[y]
        par[temp] = par_x
    par[y] = par_x


def find_minimum_edge():
    check = set()
    hp = []

    for i in range(n):
        for j in range(n):
            if (i, j) not in check and (j, i) not in check:
                if maps[i][j] and maps[j][i]:
                    # 둘 다 가중치가 있다면, 작은 애를 넣으면 됨
                    heapq.heappush(hp, [min(maps[i][j], maps[j][i]), i, j])
                elif maps[i][j] or maps[j][i]:
                    # 한 엣지만 가중치가 있다면, 걔를 넣으면 됨
                    heapq.heappush(hp, [max(maps[i][j], maps[j][i]), i, j])
                check.add((i, j))
            # 힙에 넣을 때 순서(i,j인지, j,i인지)는 크게 중요하지 않음
            # 어차피 차이는 보정이 됨

    return hp


if __name__ == "__main__":
    n = int(input())
    maps = [list(map(lambda x: ord[x], input().strip())) for _ in range(n)]
    ans = [[0] * n for _ in range(n)]

    par = [*range(n)]
    hp = find_minimum_edge()
    # 양방향이 두 개이므로 가중치가 작은 엣지만 넣어야 함. 따라서 가중치가 작은 애를 넣으면
    # 다른 애는 탐색하면 안 됨

    k = 0
    while k < n - 1:
        try:
            c, a, b = heapq.heappop(hp)
        except IndexError:
            # 힙에 남아있는 것이 없다면, 스패닝 트리를 만들 수 없음
            print(-1)
            exit(0)
        if my_par(a) != my_par(b):
            union(a, b)
            maps[a][b] -= c     # 차이를 뺌
            k += 1

    print(sum([sum(i) for i in maps]))
